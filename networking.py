import requests
import json

localBase = "http://localhost:3000"
remoteBase = "https://powerful-shelf-75482.herokuapp.com"
userSuffix = "/users"
reciverSuffix = "/main"
debug = False

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
    if res["status"] == "ok":
        token = res["token"]
        print token
        return token
    else:
        return None

def register(number,password,firstname,lastname):
    url = getBase() + userSuffix + "/register"
    data = {'number' : number, 'password' : password, 'firstName' : firstname, 'lastName' : lastname}
    r = requests.post(url,json=data)
    res = json.loads(r.text)
    if res["status"] == "ok":
        return True
    else:
        return False

def ping(number,first, token):
    print("pinging")
    url = getBase() + reciverSuffix + "/receive"
    data = {'number' : number,'first': first, 'token' : token}
    r = requests.get(url, data)
    res = json.loads(r.text)
    print res["message"]
    return res["status"]
