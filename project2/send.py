
import requests
import json
import csv

def readCSV(filename):
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        my_list = list(reader)
    return my_list

if __name__ == "__main__":
    trueFront = readCSV('2.csv')
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    addr = "http://127.0.0.1:8081/api"
    igd_list = []
    for j in range(1, 50):
        igd = 0
        for i in range(1, 40):
            frontName = "/home/st-james1/tanboxi/588_project/code/MOPSOCD/logData/2/" + str(i) + "/" + str(j) + "/front.csv"
            front = readCSV(frontName)
            data = {'trueFront':trueFront, 'front':front}
            req = requests.post(addr, data = json.dumps(data), headers = headers)
            igd = igd + float(json.loads(req.text))
        igd_list.append(igd/40)

    print igd_list
