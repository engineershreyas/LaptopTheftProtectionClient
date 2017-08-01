import requests
import json
import config

LOCAL_BASE = "http://localhost:3000"
userSuffix = "/users"
reciverSuffix = "/main"
debug = False

def getBase():
    if debug:
        return LOCAL_BASE
    else:
        return config.REMOTE_BASE

def login(number, password):
    url = getBase() + userSuffix + "/login"
    data = {'number' : number, 'password' : password}
    r = requests.post(url,json=data)
    res = json.loads(r.text)
    if res["status"] == "ok":
        token = res["token"]
        print token
        return token
    else:
        return None

def register(number,password):
    url = getBase() + userSuffix + "/register"
    data = {'number' : number, 'password' : password}
    r = requests.post(url,json=data)
    res = json.loads(r.text)
    if res["status"] == "ok":
        return True
    else:
        return False

def ping(number,first,end,token):
    print("pinging")
    url = getBase() + reciverSuffix + "/receive"
    data = {'number' : number,'first': first, 'end' : end, 'token' : token}
    r = requests.get(url, data)
    res = json.loads(r.text)
    return res["status"]
