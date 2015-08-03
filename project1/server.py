
from flask import Flask, url_for, request, Response, jsonify, json
import requests
from time import gmtime, strftime, sleep
import json




app = Flask(__name__)


@app.route('/api', methods = ['GET', 'POST'])
def hello():
	if request.method == 'GET':
            print loadLog()
	elif request.method == 'POST':
		json = request.json
		send(json)
                log(json)
                resp = make_response("", 202)
		return resp
def loadLog():
    with open("log.json") as json_file:
        json_data = json.load(json_file)
        return json_data
def log(json):
    with open('log.txt', 'w') as outfile:
        json.dump(data, outfile)

def send(data):
	msg = pack(data)
	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
	while data["order"]:
		for i in range(3):
			addr = 'http://' + data["order"][0] + ":80/api"
			try:
				print "Start trying..."
				req = requests.post(addr, data = json.dumps(msg), headers = headers, timeout = 1)
				return
			except Exception, e:
				print e
		data["order"].pop(0)
	print "failed"
	return

def pack(data):
	num = 1
	num += int(data['count'])
	data['count'] = num
	myvalue = "blasomething"
	myJson = {
            "input": data['value'],
            "output": data['value'] + myvalue,
            "time": strftime("%a, %d, %b %Y %H:%M:%S GMT", gmtime()),
            "index": len(data['audit'])
            }
	data['value'] += myvalue
	data['audit']["max"] = myJson
	return data



if __name__ == "__main__":
    import os
    try:
        PORT = int(os.environ.get('SERVER_HOST', 80))
    except ValueError:
        PORT = 80
    app.run("172.31.8.251", PORT)
