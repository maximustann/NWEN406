
import requests
import json

if __name__ == "__main__":
    with open('example.json') as data_file:
        data = json.loads(data_file.read())

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    addr = "http://54.153.185.41/api"
    req = requests.post(addr, data = json.dumps(data), headers = headers, timeout = 1)
