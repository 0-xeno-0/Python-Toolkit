#!/bin/usr/python3

import requests
import urllib3
from bs4 import BeautifulSoup

url_scheme = urllib3.PoolManager
url = 'http://192.168.185.68:8080/bijection/'
index = {'index':''}
flag = ''

for i in range(48):
	index['index'] = i
	response = requests.post(url, data = index)
	# print(response.text)
	soup = BeautifulSoup(response.text, "html.parser")
	print(soup.prettify())
	div_text=soup.find("div",{"class":"container"}).get_text()
	print(div_text)
	flag +=  div_text.strip('\n').strip()
print(flag)

