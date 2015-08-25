
import requests
import json
import csv

def readCSV(filename):
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        my_list = list(reader)
    return my_list


if __name__ == "__main__":
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    #addr = "http://54.206.0.192"
    #addr = "http://ec2-54-206-0-192.ap-southeast-2.compute.amazonaws.com/"
    addr = "http://training-2009751525.ap-southeast-2.elb.amazonaws.com/"
    proxies = {
            "http": "http://tanboxi:90909900tanN@www-cache2.ecs.vuw.ac.nz:8080",
    }
    #for pieces in data:
        #req = requests.post(addr, data = json.dumps(pieces), headers = headers, proxies = proxies)
    #req = requests.post(addr)
    for i in range(1, 5):
        filename = "/home/st-james1/tanboxi/588_project/code/MOPSOCD/logData/2/" + str(i) + '/1/front.csv'
        filename2 = '2.csv'
        front = readCSV(filename)
        trueFront = readCSV(filename2)
        data = {'front':front, 'trueFront':trueFront}
        req = requests.post(addr, data = json.dumps(data), headers = headers, proxies = proxies)
        print req

