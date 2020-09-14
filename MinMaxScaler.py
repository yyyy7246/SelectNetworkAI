from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd
from pandas import DataFrame
import csv
from collections import Counter
import matplotlib.pyplot as plt

packet = pd.read_csv('C:/16-09-23.csv')
packet = (packet[["Size", "eth.dst", "IP.src", "port.src", "eth.src", "IP.dst"]])

port = packet[["port.src"]]
df1 = port.values.tolist()
scaler = MinMaxScaler()
df1[:] = scaler.fit_transform(df1[:])

size = packet[["Size"]]
df2 = size.values.tolist()
scaler = MinMaxScaler()
df2[:] = scaler.fit_transform(df2[:])

eth_src = packet[["eth.src"]]
eth_dst = packet[["eth.dst"]]
eth_src = eth_src.values.tolist()
eth_dst = eth_dst.values.tolist()

# 여기서부터 추가 코드

ip_dst = packet[["IP.dst"]]

ip_dst = ip_dst.values.tolist()


slicing_ip_dst = []


for i in range(0, len(ip_dst)):

    slicing_ip_dst.append(ip_dst[i][0].split('.'))

ip_dst1 = []
ip_dst2 = []
ip_dst3 = []
ip_dst4 = []

for i in range(0, len(ip_dst)):
    ip_dst1.append([])
    ip_dst2.append([])
    ip_dst3.append([])
    ip_dst4.append([])

for i in range(0, len(ip_dst)):
    ip_dst1[i].append(slicing_ip_dst[i][0])
    ip_dst2[i].append(slicing_ip_dst[i][1])
    ip_dst3[i].append(slicing_ip_dst[i][2])
    ip_dst4[i].append(slicing_ip_dst[i][3])


scaler = MinMaxScaler()
ip_dst1[:] = scaler.fit_transform(ip_dst1[:])

scaler = MinMaxScaler()
ip_dst2[:] = scaler.fit_transform(ip_dst2[:])

scaler = MinMaxScaler()
ip_dst3[:] = scaler.fit_transform(ip_dst3[:])

scaler = MinMaxScaler()
ip_dst4[:] = scaler.fit_transform(ip_dst4[:])

# 여기까지 추가 코드
output = []

for i in range(0, len(eth_src)):
    if eth_src[i][0] == '18:b7:9e:02:20:44':  # Invoxia Triby Speaker
        output.append('[1,0,0]')
    elif eth_src[i][0] == 'd0:52:a8:00:67:5e' : # Samsung Smart Things
        output.append('[0,1,0]')
    elif eth_src[i][0] == '70:ee:50:18:34:43': # Netatmo Welcome Camera
        output.append('[0,0,1]')
    elif eth_src[i][0] == '30:8c:fb:2f:e4:b2': # Nest Dropcam
        output.append('[0,1,0]')
    elif eth_src[i][0] == '00:24:e4:11:18:a8': # Withings Smart Baby Monitor
        output.append('[0,0,1]')
    elif eth_src[i][0] == 'f4:f2:6d:93:51:f1': # Tplink Day Night Cloud NC220 camera
        output.append('[0,0,1]')
    elif eth_src[i][0] == '44:65:0d:56:cc:d3': # Amazon Alexa Echo
        output.append('[1,0,0]')
    elif eth_src[i][0] == '00:16:6c:ab:6b:88': # Samsung SmartCam
        output.append('[0,1,0]')
    elif eth_src[i][0] == 'ec:1a:59:83:28:11': # Belkin wemo motion sensor
        output.append('[1,0,0]')
    elif eth_src[i][0] == 'ec:1a:59:79:f4:89': # Belkin Wemo switch
        output.append('[1,0,0]')
    elif eth_src[i][0] == '08:21:ef:3b:fc:e3': # Samsung Galaxt Tab
        output.append('[1,0,0]')
    elif eth_src[i][0] == '70:5a:0f:e4:9b:c0': # HP Printer
        output.append('[0,1,0]')
    elif eth_src[i][0] == 'e0:76:d0:33:bb:85': # PIX-STAR Photo-frame
        output.append('[1,0,0]')
    elif eth_src[i][0] == '50:c7:bf:00:56:39': # TPlink Smart Plug HS105
        output.append('[1,0,0]')
    elif eth_src[i][0] == '70:ee:50:03:b8:ac': # Netamo Smart Weather Station
        output.append('[1,0,0]')
    elif eth_src[i][0] == '00:24:e4:1b:6f:96' : # Withings Body
        output.append('[0,0,1]')
    elif eth_src[i][0] == '18:b4:30:25:be:e4': # NEST Protect Smoke Alarm
        output.append('[1,0,0]')
    elif eth_src[i][0] == 'b4:ce:f6:a7:a3:c2': # Android Phone
        output.append('[0,1,0]')
    elif eth_src[i][0] == '74:2f:68:81:69:42': # Laptop
        output.append('[0,1,0]')
    elif eth_src[i][0] == 'd0:a6:37:df:a1:e1': # IPhone
        output.append('[0,1,0]')
    elif eth_src[i][0] == '74:6a:89:00:2e:25': # Blipcare Blood Pressure meter
        output.append('[0,0,1]')
    elif eth_src[i][0] == '14:cc:20:51:33:ea': # Gateway
        if eth_dst[i][0] == '18:b7:9e:02:20:44':  # Invoxia Triby Speaker
            output.append('[1,0,0]')
        elif eth_dst[i][0] == 'd0:52:a8:00:67:5e':  # Samsung Smart Things
            output.append('[0,1,0]')
        elif eth_dst[i][0] == '70:ee:50:18:34:43':  # Netatmo Welcome Camera
            output.append('[0,0,1]')
        elif eth_dst[i][0] == '00:24:e4:11:18:a8':  # Withings Smart Baby Monitor
            output.append('[0,0,1]')
        elif eth_dst[i][0] == 'f4:f2:6d:93:51:f1':  # Tplink Day Night Cloud NC220 camera
            output.append('[0,0,1]')
        elif eth_dst[i][0] == '44:65:0d:56:cc:d3':  # Amazon Alexa Echo
            output.append('[1,0,0]')
        elif eth_dst[i][0] == '00:16:6c:ab:6b:88':  # Samsung SmartCam
            output.append('[0,1,0]')
        elif eth_dst[i][0] == 'ec:1a:59:83:28:11':  # Belkin wemo motion sensor
            output.append('[1,0,0]')
        elif eth_dst[i][0] == 'ec:1a:59:79:f4:89':  # Belkin Wemo switch
            output.append('[1,0,0]')
        elif eth_dst[i][0] == '08:21:ef:3b:fc:e3':  # Samsung Galaxt Tab
            output.append('[1,0,0]')
        elif eth_dst[i][0] == '70:5a:0f:e4:9b:c0':  # HP Printer
            output.append('[0,1,0]')
        elif eth_dst[i][0] == 'e0:76:d0:33:bb:85':  # PIX-STAR Photo-frame
            output.append('[1,0,0]')
        elif eth_dst[i][0] == '50:c7:bf:00:56:39':  # TPlink Smart Plug HS105
            output.append('[1,0,0]')
        elif eth_dst[i][0] == '70:ee:50:03:b8:ac':  # Netamo Smart Weather Station
            output.append('[1,0,0]')
        elif eth_dst[i][0] == '00:24:e4:1b:6f:96':  # Withings Body
            output.append('[0,0,1]')
        elif eth_dst[i][0] == '18:b4:30:25:be:e4':  # NEST Protect Smoke Alarm
            output.append('[1,0,0]')
        elif eth_dst[i][0] == 'b4:ce:f6:a7:a3:c2':  # Android Phone
            output.append('[0,1,0]')
        elif eth_dst[i][0] == '74:2f:68:81:69:42':  # Laptop
            output.append('[0,1,0]')
        elif eth_dst[i][0] == 'd0:a6:37:df:a1:e1':  # IPhone
            output.append('[0,1,0]')
        elif eth_dst[i][0] == '74:6a:89:00:2e:25':  # Blipcare Blood Pressure meter
            output.append('[0,0,1]')
        elif eth_dst[i][0] == '01:00:5e:7f:ff:fa':  # internet Multicast mac address
            output.append('[1,0,0]')
        elif eth_dst[i][0] == 'ff:ff:ff:ff:ff:ff':  # 연결장치없음
            output.append('[1,0,0]')
        elif eth_dst[i][0] == '01:00:5e:02:00:fc':  # internet multicast mac address
            output.append('[0,1,0]')
        elif eth_dst[i][0] == '01:00:5e:00:00:fb':  # internet multicast mac address
            output.append('[0,1,0]')
        elif eth_dst[i][0] == '01:00:5e:00:00:fc':  # internet multicast mac address
            output.append('[0,1,0]')
        elif eth_dst[i][0] == '30:8c:fb:2f:e4:b2':  # Nest Dropcam
            output.append('[0,1,0]')

dflist = []
dflist2 = []
try:
    for i in range(0, 802581):
        dflist.append(df2[i])
except:
    print("e")

try:
    for i in range(0, 802581):
        dflist2.append(df1[i])
except:
    print("e")

# {"input":[1,0,0,1,0],"output":[1,0,0,0,0]}

"""
# data.json에 넣을것들
for i in range(0, 4000):
    json = '{"input":[' + str(dflist[i]).strip('[]') + '0' + ',' + str(dflist2[i]).strip('[]') + '0' + ','  + str(ip_dst1[i][0]).strip('[]') + '0' + ',' + str(ip_dst2[i][0]).strip('[]') + '0' + ',' + str(ip_dst3[i][0]).strip('[]') + '0' + ',' + str(ip_dst4[i][0]).strip('[]') + '0' + '], "output" :' + output[i] +'},'
    print(json)
"""

"""
# brain.js에 넣을것들
for i in range(4001,8000):
    json = 'console.log(net.run([' + str(dflist[i]).strip('[]') + '0' + ',' + str(dflist2[i]).strip('[]') + '0' + ',' + str(ip_dst1[i][0]).strip('[]') + '0' + ',' + str(ip_dst2[i][0]).strip('[]') + '0' + ',' + str(ip_dst3[i][0]).strip('[]') + '0' + ',' + str(ip_dst4[i][0]).strip('[]') + '0' + ']));'
    print(json)
"""


# 결과가 맞는지 확인할때
for i in range(4001,8000):
    print(output[i])
