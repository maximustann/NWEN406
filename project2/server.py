
from flask import Flask, url_for, request, Response, jsonify, json, make_response
import requests
from time import gmtime, strftime, sleep
import json as js
import threading
import atexit
import math


app = Flask(__name__)

#app.config.update(
#    CELERY_BROKER_URL='redis://localhost:6379',
#	    CELERY_RESULT_BACKEND='redis://localhost:6379'
#		)
#
#def make_celery(app):
#	celery = Celery(app.import_name, broker = app.config['CELERY_BROKER_URL'])
#	celery.conf.update(app.config)
#	TaskBase = celery.Task
#	class ContextTask(TaskBase):
#		abstract = True
#		def __call__(self, *args, **kwargs):
#			with app.app_context():
#				return TaskBase.__call__(self, *args, **kwargs)
#	celery.Task = ContextTask
#
#	return celery
#
#
#celery = make_celery(app)
#

#threads = []
@app.route('/api', methods = ['GET', 'POST'])
def hello():
	if request.method == 'GET':
		print "Hello"
		#print readLog()
	elif request.method == 'POST':
		#threads = []
		#global threads
		data = request.json
                igd = evaluate(data)
		#t = threading.Thread(target = worker, args = (data, validate(data)))
		#threads.append(t)
		#t.start()
		resp = Response(response = json.dumps(igd), status = 200, 
                                mimetype = "application/json")
		return resp

def evaluate(data):
    front = data["front"]
    trueFront = data["trueFront"]
    igd = 0
    for item in trueFront:
        igd = igd + math.sqrt(minimumEdistance(item, front))
    return igd/len(trueFront)

def minimumEdistance(item, front):
    result = []
    for instance in front:
        result.append(distance(instance, item))
    return min(result)

def distance(instance, item):
    value = (float(instance[0]) - float(item[0]))**2 + (float(instance[1]) - float(item[1]))**2
    return value

#def validate(data):
	#if 'max' in data['audit'].keys():
		#return True
	#else:
		#return False
#
#def worker(data, flag):
	#send(data, flag)
#
#def send(data, flag):
	#msg = pack(data, flag)
	#headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
	#while data["order"]:
		#for i in range(3):
			#addr = 'http://' + data["order"].pop(0) + ":80/api"
			#try:
				#print "Start sending to: " + addr
				#req = requests.post(addr, data = json.dumps(msg), headers = headers, timeout = 2)
				#if req.status_code == 202:
					#print "Send Successfully"
					#return
				#else:
					#print req
			#except Exception, e:
				#print e
	#print "No more address"
	#return
#
#@app.route('/log')
#def returnLog():
	#data = readLog()
	#return js.dumps(data)
#
#def pack(data, flag):
	#num = 1
	#num += int(data['count']) 
	#data['count'] = num
	#myvalue = "blasomething"
	#myJson = {
            #"input": data['value'],
            #"output": data['value'] + myvalue,
            #"time": strftime("%a, %d, %b %Y %H:%M:%S GMT", gmtime()),
            #"index": num - 1
            #}
	#if flag:
		#data['audit']['max'].append(myJson)
	#else:
		#myJsonList = [myJson]
		#data['audit']['max'] = myJsonList
	#data['value'] += myvalue
	#return data



if __name__ == "__main__":
    import os
    try:
        PORT = int(os.environ.get('SERVER_HOST', 8081))
    except ValueError:
        PORT = 8081
    app.run("127.0.0.1", PORT)
