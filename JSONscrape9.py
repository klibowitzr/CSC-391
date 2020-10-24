import json
import requests
import csv
csvfile = open('directory2.csv','w')
csvwriter = csv.writer(csvfile,delimiter=',')

response=requests.get("http://www.wlc.edu/WebServices/Directory.asmx/GetList?taxonomyID=183")
jsonresponse =json.loads(response.text)
#jsonData=jsonresponse[data]
for item in jsonresponse:
    fname=item.get("FirstName")
    lname=item.get("LastName")
    name=lname+", "+fname
    department=item.get("Department")
    location=item.get("Location")
    email=item.get("Email")
    phone=item.get("Phone")
    csvwriter.writerow([name, department, location, email, phone])
