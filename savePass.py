# save password
import json
from difflib import get_close_matches
import os
from os.path import isfile

data={"website": ".", "username": ".", "password": "."}

def getData():
    data={}
    data["website"]=input("Enter your website address:")
    data["username"]=input("Enter your user name:")
    data["password"]=input("Enter your password:")
    return data
def writeData(data):
    file=open("data.txt","w")
    jdata=json.load(file)
    jdata["sites"].append(data)
    file.close()
    file=open("data.txt","w+")
    json.dump(jdata,file)
    file.close()

def readData(website=None):
    try:
        file=open("data.txt","r")
        sites=json.load(file)
        file.close()
        if(website):
            for site in sites["sites"]:
                 if site["website"]==website:
                     return site
            else:
                 return sites
    except:
        print("couldnt open file")
        return []


def printResult(data):
    for x in data:
        print(x,":",data[x])
        print("")
    print("<<<<job successfully done>>>>")



def askName():
    siteName=input("enter website name:")
    sites=readData()
    siteNames=[]
    for site in sites["sites"]:
         siteNames.append(site["website"])
    
    if len(get_close_matches(siteName,siteNames) and len(sites)>0)>0:
        yn=input("did you mean %s ?y/n   "%get_close_matches(siteName,siteNames)[0])
        if (yn=="y"):
             return {"status":"200","data":get_close_matches(siteName,siteNames)[0]}
        else:
             yn=input("its new site?y/n")
             if yn=="y":
                 return {"status":"202","data":[]}
    else:
        yn=input("its new site?y/n")
        if yn=="y":
             return {"status":"202","data":[]}

def file_exist():
    return isfile("data.txt")


#check data.txt file exist
if not file_exist():
    q=input("data.txt file are not available .create a new one?y/n  ")
    if q=="y":
            writeData(data)

#this is main loop
while(True):
    site=askName()
    if (site["status"]=="200"):
        printResult(readData(site["data"]))
    elif (site["status"]=="202") :
        writeData(getData())


