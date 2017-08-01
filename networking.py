import requests
import json

localBase = "http://localhost:3000"
remoteBase = "https://idk.com"
userSuffix = "/users"
reciverSuffix = "/main"
debug = True

def getBase():
    if debug:
        return localBase
    else:
        return remoteBase

def login(number, password):
    url = getBase() + userSuffix + "/login"
    data = {'number' : number, 'password' : password}
    r = requests.post(url,json=data)
    res = json.loads(r.text)
    if res.status is "ok":
        token = res.token
        print token
        return token
    else
        print res.message
        return None

def register(number,password,firstname,lastname):
    url = getBase() + userSuffix + "/register"
    data = {'number' : number, 'password' : password, 'firstName' : firstname, 'lastName' : lastname}
    r = requests.post(url,json=data)
    res = json.loads(r.text)
    if res.status is "ok":
        return True
    else
        print res.message
        return False

def ping(number,token):
    url = getBase() + reciverSuffix + "/receive"
    data = {'number' : number,'token' : token}
    r = requests.get(url, data)
    res = json.loads(r.text)
    print res.message
    return res.status
