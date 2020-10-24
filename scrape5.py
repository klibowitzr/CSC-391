#! /usr/bin/env python

# this demonstrates how to log into a website.   It is very fragile but
# the goal is to demonstrate how to deal with forms, submit them, and
# use a session to maintain cookies across page reads
# this program assumes that you've done the research and you know what
# fields you need to fill in

import sys
import requests
import lxml
import getpass
from bs4 import BeautifulSoup

sys.path.append("../lib")
from agentsGalore import agentsGalore
from formHelper import formHelper

# start a session
session = requests.Session()
ag = agentsGalore()


def openURL(url,cookie=None):
    global session
    global ag
    headers = ag.makeHeader("MacFirefox58","default","default","langUS")
    try:
        if cookie:
            r = session.get(url, cookies=cookie, headers=headers)
        else:
            r = session.get(url, headers=headers)
    except requests.exceptions.RequestException as e:
        print(e)
        exit(1)

    return r

# this function does a POST to the URL with the params in a hash
def postURL(url,params):
    global ag
    global session
    headers = ag.makeHeader("MacFirefox58","default","default","langUS")
    try:
        r = session.post(url, data=params)
    except requests.exceptions.RequestException as e:
        print(e)
        exit(1)

    return r

# first open the login page
url = "https://my.wlc.edu/ICS/"

resp = openURL(url)
fh = formHelper(resp.text)

# get a populated param structure.  You can call fh.analyzeInputs() to
# see what all the input fields are.  See sample in ../lib/formHelper.py
params = fh.populateFormInputs(fh.getFormById("MAINFORM"))

userid   = getpass.getpass("enter your userid:",sys.stderr)
password = getpass.getpass("enter your password:",sys.stderr)

params['userName'] = userid
params['password'] = password

formurl = "https://my.wlc.edu/ICS"
res = postURL(formurl,params)

# todo:  check that this actually worked.

print(res.text)
