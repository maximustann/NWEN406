
from flask import Flask, url_for, request, Response, jsonify, json, make_response
import requests
from time import gmtime, strftime, sleep
import json as js




app = Flask(__name__)


@app.route('/api', methods = ['GET', 'POST'])
def hello():
	if request.method == 'GET':
		print "Hello"
		#print readLog()
	elif request.method == 'POST':
		data = request.json
		resp = make_response('', 202)
		return resp

def showData(data):
    print data
#def log(data):
	#with open('log.json', 'w') as outfile:
		#js.dump(data, outfile)

#def send(data):
	#msg = pack(data)
	#headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
	#while data["order"]:
		#for i in range(3):
			#addr = 'http://' + data["order"].pop(0) + ":80/api"
			#try:
				#print "Start trying..."
				#req = requests.post(addr, data = json.dumps(msg), headers = headers, timeout = 2)
				#if req.status_code == 202:
					#print "Send Successfully"
					#return
			#except Exception, e:
				#print e
	#print "failed"
	#return

#@app.route('/log')
#def returnLog():
	#data = readLog()
	#return js.dumps(data)

#def pack(data):
	#num = 1
	#num += int(data['count'])
	#data['count'] = num
	#myvalue = "blasomething"
	#myJson = {
            #"input": data['value'],
            #"output": data['value'] + myvalue,
            #"time": strftime("%a, %d, %b %Y %H:%M:%S GMT", gmtime()),
            #"index": len(data['audit'])
            #}
	#data['value'] += myvalue
	#data['audit']["max"] = myJson
	#return data



if __name__ == "__main__":
    import os
    try:
        PORT = int(os.environ.get('SERVER_HOST', 80))
    except ValueError:
        PORT = 80
    app.run("172.31.8.251", PORT)
