# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 23:45:59 2015

@author: akhan
"""

from bs4 import BeautifulSoup
import requests
import re

url="www.google.com/finance"
r=requests.get("http://"+url)
soup=BeautifulSoup(r.text)

table=soup.find("div",{"id":"secperf"})

names=[]
percent=[]
myitems=table.find_all("a")

for item in myitems:
    names.append(item.text)

for item in table.find_all("span"):
    percent.append(abs(float(item.text.replace("%",""))))


links=[]
for item in table.find_all("a"):
    links.append(item.get("href"))

import numpy
max_ind=numpy.argmax(percent)
newUrl="www.google.com"+links[max_ind]
r2=requests.get("http://"+newUrl)
soup2=BeautifulSoup(r2.text)
topmovers=soup2.find("table",{"class":"topmovers"})

names2=[]
percent2=[]

for item in topmovers.find_all("a"):
    names2.append(item.text)

for item in topmovers.find_all("span"):
    #    percent2.append(abs(float(item.text.replace("%",""))))
    percent2.append(item.text.replace("%",""))    

names2=names2[0::2]
percent2=percent2[1::2]
percent2=map(lambda x:float(x.replace("(","").replace(")","")),percent2)
print "Max :",names2[numpy.argmax(percent2)]
print "Min :",names2[numpy.argmin(percent2)]
#data=r.text
#print data
#txt=re.compile("secperf")
#soup.