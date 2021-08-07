# save password
import json
from difflib import get_close_matches
import os
from os.path import isfile

data={"website": ".", "username": ".", "password": "."}

def get_data():
    data={}
    data["website"]=input("Enter your website address:")
    data["username"]=input("Enter your user name:")
    data["password"]=input("Enter your password:")
    return data
def write_data(data):
    file=open("data.txt")
    jdata=json.load(file)
    jdata["sites"].append(data)
    file.close()
    file=open("data.txt","w+")
    json.dump(jdata,file)
    file.close()

def read_data(website=None):
    file=open("data.txt","r")
    sites=json.load(file)
    file.close()
    if(website):
        for site in sites["sites"]:
             if site["website"]==website:
                 return site
    else:
         return sites

def print_result(data):
    for x in data:
        print(x,":",data[x])
        print("")
    print("<<<<job successfully done>>>>")

def ask_name():
    siteName=input("enter website name:")
    sites=read_data()
    siteNames=[]
    if sites:
        for site in sites["sites"]:
             siteNames.append(site["website"])
    if len(get_close_matches(siteName,siteNames))>0:
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

def creat_container():
    sites={"sites":[]}
    file=open("data.txt",'w+')
    jstring=json.dumps(sites)
    file.write(jstring)
    file.close()

#check data.txt file exist
if not file_exist():
    creat_container()   
#this is main loop
while(True):
    site=ask_name()
    if (site["status"]=="200"):
        print_result(read_data(site["data"]))
    elif (site["status"]=="202") :
        write_data(get_data())
        print("your data stored successfully")


