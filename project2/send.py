
import requests
import json
import csv

def readCSV(filename):
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        my_list = list(reader)
        for item in my_list:
            print item


if __name__ == "__main__":
    readCSV("./2.csv")
    #headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    #addr = "http://54.153.185.41/api"
    #req = requests.post(addr, data = json.dumps(data), headers = headers, timeout = 1)
