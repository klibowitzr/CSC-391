import sys
import getpass
import time
import os
import lxml
import csv
import re
import textwrap
import base64
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from myWebDrivers import myWebDrivers
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


###THIS BLOCK OF CODE NAVIGATED TO NYT, GRABBED
##THE PAGE SOURCE, AND SAVED THE HTML TO A FILE USING SELENIUM
# myhome=os.environ['HOME']
# mwd=myWebDrivers(myhome, 'firefox', False)
# #driver = webdriver.Firefox(executable_path=r'/Users/rkibs98/Desktop/geckodriver.exe')
# mwd.setImplicitWait(10)
# driver=mwd.getDriver()
# mwd.get("https://www.nytimes.com/2018/11/05/us/jayme-closs-missing-girl-barron-wisconsin.html?action=click&module=Top%20Stories&pgtype=Homepage")
# time.sleep(1)
# # mwd.setImplicitWait(10)
#
# mwd.savePageSource("Closs.html")
sys.path.append("deslib")
sys.path.append("lib")
#Again, I don't know if I did this correctly

html=soup(open("Closs.html"), "lxml")
heading=html.find('body').find('h1', class_="css-fui35v ejekc6u0").get_text()
print(heading)
print("")
subheading=html.find('body').find('p', class_='css-1ux7ruj ewc5vgb0').get_text()
print(subheading)
print("")
authorinfo=html.find('body').find('p', class_='css-jvmkce e1x1pwtg1')
authorline=authorinfo.get_text()
print(authorline)
print("")
date=html.find('body').find('time', class_='css-1wnyjki eqgapgq0').get_text()
print(date)
print("")
text=html.find('body').findAll('p', class_='css-1xl4flh e2kc3sl0')
for p in text:
    print(p.get_text())
print("")
print("")
print("List of articles from the front page of the New York Times:")
print("")



#THIS BLOCK OF CODE FOUND ALL ARTICLES ON THE NYT'S FRONT PAGE, THESE STORIES
#ARE SLIGHLTY OUTDATED.
# myhome=os.environ['HOME']
# mwd=myWebDrivers(myhome, 'firefox', False)
# #driver = webdriver.Firefox(executable_path=r'/Users/rkibs98/Desktop/geckodriver.exe')
# mwd.setImplicitWait(10)
# driver=mwd.getDriver()
# mwd.get("https://www.nytimes.com")
# time.sleep(1)
# # mwd.setImplicitWait(10)
#
# mwd.savePageSource("NYT.html")
doc = soup(open("NYT.html"), "lxml")
# print(doc)
# links=doc.find('body').find_all("h2", class_="css-1lnv2oj esl82me2")#, class_="css-78b01r esl82me2", class_="css-tu3ssm esl82me2", class_="css-c5hz4q esl82me2", class_="css-jeabx6 esl82me2")
# #links=doc.find('body').findAll(attrs={'class':["css-1lnv2oj esl82me2","css-78b01r esl82me2","css-tu3ssm esl82me2", "css-c5hz4q esl82me2","css-jeabx6 esl82me2"]})
# for h2 in links:
#     print(h2.find("span").get_text())
#     print("")
# links2=doc.find('body').find_all("h2", class_="css-78b01r esl82me2")
# for h2 in links2:
#     print(h2.find("span", class_="ghost").get_text())
#     print("")
# links3=doc.find('body').find_all("h2", class_="css-tu3ssm esl82me2")
# for h2 in links3:
#     print(h2.find("span").get_text())
#     print("")
# links4=doc.find('body').find_all("h2", class_="css-c5hz4q esl82me2")
# for h2 in links4:
#     print(h2.find("span").get_text())
#     print("")
# links5=doc.find('body').find_all("h2", class_="css-jeabx6 esl82me2")
# for h2 in links5:
#     print(h2.find("span").get_text())
#     print("")

# links7=doc.find('body').find_all("h2", class_="css-8uvv5f esl82me2")
# for h2 in links7:
#     print(h2.get_text())
#     print("")

main=doc.find('body').find_all("h1", class_="eln-banner-headline")
for h1 in main:
    print(h1.get_text())
    print("")

alllinks=doc.find('body').find_all("div", class_="css-1j836f9 esl82me3")
for div in alllinks:
    print(div.find('h2').get_text())
    print("")
# doc = soup(open("NYT.html"), "lxml")
# links=doc.find('body').find("h2", text="A dazzling duck appeared in Central Park. Read about it in The Week in Good News.")
# print(links.get_text())
