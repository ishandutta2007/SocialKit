import time
import random
import queue
import threading
from API.instagram_private_api import Client


api = Client(
    auto_patch=True, authenticate=True,
    username="username", password="password")

def login():

    api = Client(
    auto_patch=True, authenticate=True,
    username="communism", password="vlad")
    return api

COUNT = 0

#add a comment

class MyThread(threading.Thread):
    def __init__(self, q, name, n, lst):
        threading.Thread.__init__(self)
        self.lst = lst
        self.name = name
        self.n = n
        self.q = q

    def run(self):
        #print("{}: STARTING".format(self.name))
        accept(self.name, self.n, self.lst, self.q)
        #print("{}: EXITING".format(self.name))


def get_list():
    pending = api.friendships_pending()["users"]
    lst=[]
    for user in pending:
        lst.append(user["pk"])

    return lst


def splitter(arr, size):
    arrs = []
    while len(arr) > size:
        piece = arr[:size]
        arrs.append(piece)
        arr = arr[size:]
    arrs.append(arr)
    return arrs


def accept(name, n, lst, q):
    q.put(n)
    randtime = random.randint(1, 10)
    randtime = randtime / 10
    api.approve(lst[n][0])
    time.sleep(randtime / 100)
    global COUNT
    COUNT+=1
    q.get(n)
    print("{}: Accepted {} followers.".format(name, COUNT))
    return None


def combine():

    q = queue.Queue(200)
    pks = get_list()
    split = splitter(pks, 1)
    print("Starting...")
    start = time.time()
    seen = set()
    seen.update(pks)
    while pks != []:
        for i in range(len(split)):
            thread = MyThread(q, "Thread-{}".format(i), i, split)
            thread.start()

        time.sleep(1)

        pks = get_list()
        pks = [pk for pk in pks if pk not in seen]
        if not pks: break
        split = splitter(pks, len(split))

    end = time.time()

    elapsed = (end-start)
    return "Done. Time elapsed: {}".format(elapsed)
