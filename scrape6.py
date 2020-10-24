import sys
import getpass
import time
import os
import lxml
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
bsobj=soup(mwd.getPageSource(), "lxml")
maintbl=bsobj.find('body').find('div', class_="pSection").table.findAll("a")#.find('td', style_="while-space:nowrap;")
for a in maintbl:
    name=a.get_text()
    print(name)
mwd.quit()
#namelist=maintbl.findAll("a").get_text();
#for a in trs:
#    print(a.get_text())
#for tr in maintbl:
    #print(tr.find_All("a").get_text())
#for a in maintbl:
##    print(name.get_text())
#name=maintable.find("td",{"style":"white-space::nowrap"}).find("a")
#maintable=bsObj.find(id_="pg0_V_tblUsers").find("tbody")
        #print (name.get_text())
        #print('\n')
