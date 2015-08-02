
from flask import Flask, url_for, request, Response, jsonify, json
import requests
from time import gmtime, strftime, sleep




app = Flask(__name__)
data = None
# Make the WSGI interface avaiable a the top level so wfastcgi can get it 
wsgi_app = app.wsgi_app

@app.route('/api', methods = ['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return "Hello, world"
    elif request.method == 'POST':
        if check(request.json):
            return "201"
        else:
            return "400"

def check(rec):
    global data
    data = rec
    return True

@app.teardown_appcontext
def send(exception):
    global data
    msg = pack(data)
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    while True:
        for i in range(3):
            addr = 'http://' + data["order"][0] + ":5555/api"
            try:
                req = requests.post(addr, data = json.dumps(msg), headers = headers, timeout = 0.001)
                return
            except Exception, e:
                print e
        data["order"].pop(0)
    return

def pack(data):
    data['count'] += 1
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
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_HOST', 5556))
    except ValueError:
        PORT = 5556
    app.run(HOST, PORT)
