#!/usr/bin/python3

import os
import time
import datetime
import socket


# 31/12/2020 %d/%m/%Y
# 12/31/2020 %m/%d/%Y
# 12312020   %m%d%Y
def getTimeStamp(dateString):
    return time.mktime(datetime.datetime.strptime(dateString, "%m%d%Y").timetuple())

def postMetrics(metricHeader, metrics):
    graphiteIP = 'localhost'  # 'graphite'
    graphitePort = 2003       # Plaintext protocol: <metric path> <metric value> <metric timestamp>
    metricPath = "Sedgwick.Covid"
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)        # timeout 5 seconds
    try:
        sock.connect((graphiteIP, graphitePort))
        timeStamp = getTimeStamp(metrics[0])
        # Sedgwick.Covid.Date 04122020 1586667600.0
        # Sedgwick.Covid.Cases 196 1586667600.0
        # Sedgwick.Covid.Recoveries 74 1586667600.0
        for header, metric in zip(metricHeader, metrics):
            msg = '{}.{} {} {}\n'.format(metricPath, header, metric, timeStamp)
            print(msg)
            sock.send(msg.encode('utf-8'))
            time.sleep(0.005)  # 5 ms
        sock.close()
    except:
        print("Covid data not posted to Graphite")
        pass

def postData():
    dataPath = os.path.dirname(os.path.realpath(__file__))
    try:
        with open('{}/sedgwick_covid.data'.format(dataPath), 'r') as dataFile:
            firstLine = dataFile.readline()
            dataHeader = firstLine.strip().split(' ')
            for line in dataFile:
                items = line.strip().split(' ')
                if len(items) == 3:
                    covidCases = [str(items[0]), int(items[1]), int(items[2])]
                    postMetrics(dataHeader, covidCases)
    except Exception as e:
        print("Error getting data: {}".format(e))

if __name__ == '__main__':
    postData()

