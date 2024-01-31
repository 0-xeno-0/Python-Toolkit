#!/usr/bin/python3

import argparse
import requests


# URL = input("[!] Enter the target URL to crawl : ").strip()
# domain = input("[!] Enter the target domain : ").strip()
def get_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", dest="URL", help="Enter, URL to crawl : ")
    option = parser.parse_args()
    if not option.URL:
        parser.error("[-] Please specify the URL. Use --help for more info : ")
        return option


def containerList():
    urlList = []
    return urlList


def containerDict():
    isFollowed = {}
    return isFollowed


def checkURL(URL):
    if URL in containerList():
        return True
    else:
        return False


def isFollowedCheck(URL):
    if checkURL(URL):
        for entry in containerDict().keys():
            if URL != entry:
                return False
            else:
                if containerDict()[URL] == "yes":
                    return True
                else:
                    return False


def listMaintainer(URL):
    if not isFollowedCheck(URL):
        containerList().append(URL)
        return True
    else:
        return True


def urlChecker(URL):
    if listMaintainer(URL):
        for uri in containerList():
            if not isFollowedCheck(URL):
                page = requests.get(uri)
                containerDict()[uri] = "yes"

                start = "http"
                for line in page.text.split("\n"):
                    if "http" in line:
                        if "google" in line:
                            if "\">" in line:
                                end = "\">"
                            else:
                                end = "\" "
                            sliced = line[line.index(start):line.index(end)]
                            if "\"" in sliced:
                                end = "\""
                                parsedURL = sliced[sliced.index(start):sliced.index(end)]
                            else:
                                parsedURL = sliced
                            return parsedURL


def checkUrlList(URL):
    if not urlChecker(URL):
        containerList().append(urlChecker(URL))
        containerDict()[urlChecker(URL)] = "no"
        return True


def output(URL):
    if checkUrlList(URL):
        for URL in containerList():
            print(URL)


arguments = get_argument()
output(arguments)
