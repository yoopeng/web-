import requests
import re
import time,os
a=requests.session()

aa='fsagar+rgfgdfdga'
b=re.search('r(.+?)rgfg',aa)
print(b)



# time1=time.gettime()
time=time.strftime('%Y-%m-%d %H:%M:%S')
print(time)

a1=os.getcwd()

path=os.path.dirname(os.path.dirname(__file__))
print(a1,path)