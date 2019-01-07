import requests
import threading
import time
from API.instagram_private_api import Client
import json


def request():
    r=requests.get("https://instagram.fxds1-1.fna.fbcdn.net/vp/e7b2152cd92f3ff3e7358db8e6a986f2/5CB93A28/t51.2885-19/s150x150/47584440_2444749568921559_1889792593856823296_n.jpg?_nc_ht=instagram.fxds1-1.fna.fbcdn.net", headers=headers)
    return r

headers={
    "authority":"instagram.fxds1-1.fna.fbcdn.net",
    "path":"/vp/75a2143cd220b2fecca1673ac5987101/5CB64CF1/t51.2885-19/44884218_345707102882519_2446069589734326272_n.jpg?_nc_ht=instagram.fxds1-1.fna.fbcdn.net",
    "scheme":"https",
    "referer":"https://www.instagram.com/holyvlad1/"
}


for i in range(1000):
    r=request()
    print(r)