import requests
from API.instagram_private_api import Client
import threading
import json
import time


initial_url = "https://www.instagram.com/accounts/emailsignup/"
url = "https://www.instagram.com/accounts/web_create_ajax/attempt/"
cookie = open("cookie.txt").read()

self_user = str(input("Enter your Instagram username here: "))
self_pass = str(input("Enter your Instagram password here: "))


class MyThread(threading.Thread):
    def __init__(self, i):
        threading.Thread.__init__(self)
        self.i = i

    def run(self):
        try:
            check(self.i)
        except:
            print("ERROR: could not do it.")

try:
    api = Client(
        auto_patch=True, authenticate=True,
        username=self_user, password=self_pass)
except:
    try:
        api = Client(
            auto_patch=True, authenticate=True,
            username=self_user, password=self_pass)
    except:
        print("Something is wrong! Either your username and password are incorrect, "
              "or you aren't connected to the Internet.")
        exit(-1)

print("Logged in.")


self_email = api.current_user()["user"]["email"]
self_gender = api.current_user()["user"]["gender"]
c_u = api.current_user()["user"]["username"]
o_u = str(input("Enter the username you wish to change to: "))
t_i = None
got = False
c = 0

proxy = open("proxy.txt").read().splitlines()

while not t_i:
    try:
        t_i = int(input("Enter time interval(ms): "))
    except:
        print("Make sure you enter an integer!")

def headers(cookie, crf):
    headers =   {"authority": "www.instagram.com",
                "method": "POST",
                "path": "/accounts/web_create_ajax/attempt/",
                #"scheme": "https",
                "accept": "*/*",
                 "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US, en;q=0.9",
                 "content-length": "70",
                 "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                 "cookie": cookie,
                 "origin": "https://www.instagram.com",
                 "referer": "https://www.instagram.com//accounts/emailsignup",
                 "Request-Timeout":"8000",
                 "Keep-Alive":"True",
                 "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
                 "x-csrftoken": crf,
                 #"x-instagram-ajax": "4ff2dd661008",
                 "x-requested-with":"XMLHttpRequest"
           }
    return headers


def gencookie():
    obj = requests.get("https://www.instagram.com/accounts/web_create_ajax/attempt/").cookies._cookies[".instagram.com"]["/"]
    full = "mid={}; rur=FRC; mcd=3, csrftoken={}".format(obj["mid"].value, obj["csrftoken"].value)
    csrf = obj["csrftoken"].value

    return (full, csrf)

def payload():
    payload ={"email":"randomunclaimedemail@payload.com",
          "password":str(c)+"100000123",
          "username":o_u,
          "first_name":"REAVERS",
          "opt_into_one_tap":"false"
          }
    return payload

pl1 = "email=awdawdawd%40gmail.com&password=vladawdaaa&username="+o_u+"&first_name=awda&opt_into_one_tap=false"

pl = json.dumps(pl1).encode("ascii")

by = json.dumps(payload()).encode("ascii")


def request(proxies):
    global got, c
    ch = False
    while not ch:
        ch = requests.post(url, headers=headers(gencookie()[0], gencookie()[1]), data=pl, proxies=proxies).json()["dryrun_passed"]
        print(ch)
        time.sleep(0.5)
    got = True
    changer()
    print("Success! Username has been claimed.")
    exit(0)
    c += 1
    return ch


def changer():
    api.change_user(o_u, self_email, self_gender)


def check(man):
    global got, c, t_i



    try:
        ch = request({"https":proxy[man]})
        time.sleep(1)
        c += 1
        print("PASSED")
    except:
        proxy.pop(man)
        print("FAILED")

    got = True
    changer()
    print("Success! Username has been claimed.")
    exit(0)
    c += 1
    return ch



print("Initiating...")



print("Starting script... press CTRL+C to stop before it gets the name.")
for i in range(t_i):
    thread = MyThread(i)
    try:
        thread.start()
        print("REAVERS: {} PASSED.".format(c))
    except:
        print("REAVERS: {} FAILED.".format(c))
    i+=1
    #time.sleep(t_i/1000)

exit(0)