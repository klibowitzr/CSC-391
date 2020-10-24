import sys
import requests
import lxml
import getpass
from bs4 import BeautifulSoup

class formHelper:
    def __init__(self,webpage):
        self.soup = BeautifulSoup(webpage,"lxml")

    def analyzeInputs(self,form):
        if form.has_attr("id"): print(form["id"],end=" ")
        if form.has_attr("name"): print(form["name"],end=" ")
        print()
        print("Inputs Fields")
        inputs = self.getInputFields(form)
        for input in inputs:
            print(end=" ")
            if input.has_attr("id"):
                print(input["id"],end=" ")
            if input.has_attr("name"):
                print(input["name"],end=" ")
            if input.has_attr("value") and len(input["value"])>0:
                print(input["value"])
            else:
                print("<EMPTY>")

    def getForms(self):
        forms = self.soup.find_all("form")
        return forms

    def getFormById(self,id):
        return self.soup.find("form",{"id":id})

    def getInputFields(self,form):
        inputs = form.find_all("input")
        return inputs

    def populateFormInputs(self,f):
        params = {}
        inputs = self.getInputFields(f)
        for input in inputs:
            if input.has_attr("name"):
                if input.has_attr("value") and len(input["value"])>0:
                    params[input["name"]] = input["value"]
                else:
                    params[input["name"]] = ""

        return params


if __name__ == '__main__':
    session = requests.Session()
    url = "https://my.wlc.edu/ics"
    resp = session.get(url)
    
    fh = formHelper(resp.text)

    print("Checking for Forms")
    forms = fh.getForms()
    num = 1
    for f in forms:
        print(num,f["name"])
        num += 1

    print("Analyzing Form Inputs")
    num = 1
    for f in forms:
        print ("form",num)
        fh.analyzeInputs(f)
        num += 1

    print("Printing Parameter Structure")
    #params = fh.populateFormInputs(forms[0])
    params = fh.populateFormInputs(fh.getFormById("MAINFORM"))
    for p in params.keys(): 
        print(" ",p,"->",params[p])

