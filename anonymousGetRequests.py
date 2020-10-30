from subprocess import call
import time
import random
import sys
from urllib.request import urlopen
from json import load
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


URL = sys.argv[0]
#Call requests infinite loop
try:
    while True:
        call(["python", "request.py",URL])
        wait = random.randint(2,15)
        time.sleep(wait)

except KeyboardInterrupt:
    print('Interrputed... Closing Requests')
    print('Exported IP List File')


##ANALIZE YOUT PROXY REQUESTS ##

def ipInfo(addr=''):
    '''
    Get IP info from ip addres
    '''
    if addr == '':
        url = 'https://ipinfo.io/json'
    else:
        url = 'https://ipinfo.io/' + addr + '/json'
    time.sleep(2)
    res = urlopen(url)
    #response from url(if res==None then check connection)
    data = load(res)
    return data, res

ips = []
f = open("ip_list.txt", "r")
for x in f:
    ips.append(x.split(",")[1].replace("\n",""))
f.close()

data_list = []
for i in range(len(ips)):
    if i == 10: # ANALYZE JUST FIRST 100 IPS AS ITS MANY COMPUTATIONAL TIME AND IT CAN BE COSNIDERED A DDOS
        break;
    data, res = ipInfo(ips[i])
    data_list.append([ips[i],data['city'],data['country'],data['region']])
    print("Getting IP: " + str(i) )
df = pd.DataFrame(data_list,columns = ['Ip Adress','City','Country','Region'])
df['Country'].hist(figsize  = (20,10))
