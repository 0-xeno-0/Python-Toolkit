#!/usr/bin/python3

import re
import requests
import urllib3
from urllib.request import urlopen
from bs4 import BeautifulSoup

# URL = input("Enter the target URL : ")
# domain = URL.split("/")
# urlList = []
# isFollowed = {}

# def checkUrlList(URL):
#    if URL in urlList:
#        return True
#    else:
#        return False

# def isFollowedCheck(URL):
#    for entry in isFollowed.keys():
#        if URL != entry:
#            return False
#        else:
#            if isFollowed[URL] == "yes":
#                return True
#            else:
#                return False
                               
# urlList.append(URL)

# for URL in urlList:
#    if isFollowedCheck(URL) != True:
#        page = requests.get(URL)
#        isFollowed[URL] = "yes"
       
#        start = "http"
#        for line in page.text.split("\n"):
#            if "http" in line:
#                if domain[2] in line:
#                    if "\">" in line:
#                        end = "\">"
#                    else:
#                        end = "\" "
#                    sliced = line[line.index(start):line.index(end)]
#                    if "\"" in sliced:
#                        end = "\""
#                        parsedURL = sliced[sliced.index(start):sliced.index(end)]
#                    else:
#                        parsedURL = sliced
#                    if checkUrlList(parsedURL) == False:
#                        urlList.append(parsedURL)
#                        isFollowed[parsedURL] = "no"

# url = urlopen("http://192.168.243.68:8080/crawling")
# # for url in urlList:
# page = url.read()
# soup = BeautifulSoup(page, features="html.parser")

# print(soup)

url_scheme = urllib3.PoolManager()
url = 'http://192.168.185.68:8080/about.html'
response = url_scheme.request('Get', url)
print(response.data.decode())
urlList = []

x = re.findall('(?:<tr>)(.*?)</tr>', response.data.decode())
for i in x:
    y = url + i
    urlList.append(y)
    for j in urlList:
        get = urlopen(j)
        # for url in urlList:
        page = get.read()
        soup = BeautifulSoup(page, features="html.parser")
        # print(re.findall('(?:OS{)(.*?)}', str(soup)))
# print(urlList)

# html_text = requests.get('http://192.168.243.68:8080/table').text

# soup = BeautifulSoup(html_text, 'lxml')
# flag = soup.find_all('tr', class_ = 'table')
# for x in flag:
#     x_name = x.select_one('a[class="AnchorLink leaderboard_player_name"]').get_text(strip=True)
#     x_score = x.select_one('td.Table__TD:nth-child(4)').get_text(strip=True)
#     print(f'{x_name} final score {x_score}')