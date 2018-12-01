from API.instagram_private_api import Client
import time
import random

with open("config.txt") as infile:
    user, password, debug = [line.strip() for _, line in zip(range(3), infile)]

api = Client(user, password)
pending = api.friendships_pending()

total = 0
while pending["users"]:
    for user in pending["users"]:
        randtime=random.randint(1,10)
        randtime=randtime/10
        api.approve(user["pk"])
        total+=1
        print("Accepted:", total, end="\n", flush=True)
        time.sleep(randtime/100)
    pending = api.friendships_pending()
print("Accepted:", total, end='\r', flush=True)