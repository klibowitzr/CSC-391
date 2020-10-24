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

myhome=os.environ['HOME']
mwd=myWebDrivers(myhome, 'firefox', False)
#driver = webdriver.Firefox(executable_path=r'/Users/rkibs98/Desktop/geckodriver.exe')
mwd.setImplicitWait(10)
driver=mwd.getDriver()
mwd.get("https://my.wlc.edu/ics")
time.sleep(1)
input("Press a key to continue")
toggle = driver.find_element_by_id("siteNavBar_loginToggle")
if toggle.is_displayed():
    print("mobile screen")
    toggle.click()
else:
    print("normal screen")
mainform = driver.find_element_by_id('MAINFORM')
mwd.printVisibleFormFields(mainform)
input("press a key to continue")

userid = input("Enter user id ")
passwd = getpass.getpass("Enter your password: ")

driver.find_element_by_name('userName').send_keys(userid)
driver.find_element_by_name('password').send_keys(passwd)
input("press enter to submit")

# this submits the login form
driver.find_element_by_name('siteNavBar$btnLogin').click()
input("press a key to load welcome mat")
mwd.get("https://my.wlc.edu/ICS/Campus_Life/Welcome_Mat.jnz")
driver=mwd.getDriver();
select = Select(driver.find_element_by_id('pg0_V_ddlStudentType'))
input("press enter to select 'All Students'")

select.select_by_value('AL')
input("press enter to submit this selection")

driver.find_element_by_id('pg0_V_btnSelect').click()
input("press a key to verify that welcome mat opened")
if driver.find_element_by_id("contextName").get_attribute('innerHTML')=="Welcome Mat":
    print("Welcome Mat loaded successfully")
else:
    print("Welcome Mat did not load successfully")
time.sleep(1)
#make picture directory
picturedir = os.path.join(os.getcwd(),"pictures")
if not os.path.isdir(picturedir):
    print ("Creating",picturedir)
    os.mkdir(picturedir)
else:
    print (picturedir,"already exists")
# create your CSV file
csvfile = open('students.csv','w')
csvwriter = csv.writer(csvfile,delimiter=',')

bsobj=soup(mwd.getPageSource(), "lxml")
maintbl=bsobj.find('body').find('div', class_="pSection").table.findAll("a")#.find('td', style_="while-space:nowrap;")
for a in maintbl:
    corpus=a.get('id')
    pattern="pg0_V_lnk"
    sid=re.sub(pattern, "", corpus)
    name=a.get_text()
    standing=a.parent.parent.parent.span.get_text()
    csvwriter.writerow([name,sid, standing])
    imagebank=a.parent.parent.parent.find("img") #moves up tree to find
    #corresponding image
    corpus2=imagebank.get('src')
    if corpus2!="/ICS/UI/Common/Images/PortletImages"+\
    "/Icons/32/missing_user_photo_32.png":
            #if the student's image is the default it is not created, skips code
            #Inside of the rest of the loop
        pattern2="data:image/jpg;base64,"
        url=str(re.sub(pattern2, "",corpus2))
        #newurl=url[0:-4] #takes off last four characters, in some cases
        #this seemed to be unneedeed but in others it seems to be needed. In
        #the myWLC version of Mandy's photo there is four characters that are
        #not present at the end of the one you posted
        deurl=base64.standard_b64decode(url)
        #decodes base64 into a 'readable' link
        pattern3=" "
        jpgname=re.sub(pattern3, "_", name)
        #replaces space in name with underscore
        jpgname=picturedir+"/"+jpgname+".jpg"
        #creates image name and image
        #print(jpgname)
        fd=open(jpgname, 'wb')
        fd.write(deurl)
        fd.close()
mwd.quit()
#closes web browser
