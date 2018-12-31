import time
import random
import queue
import threading
from Bots.Functions.API import login


api = login.login()

COUNT = 0

class MyThread(threading.Thread):
    def __init__(self, q, name, n, lst):
        threading.Thread.__init__(self)
        self.lst = lst
        self.name = name
        self.n = n
        self.q = q

    def run(self):
        print("{}: STARTING".format(self.name))
        accept(self.name, self.n, self.lst, self.q)
        print("{}: EXITING".format(self.name))


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
    for i in range(len(lst[n])):
        randtime = random.randint(1, 10)
        randtime = randtime / 10
        api.approve(lst[n][i])
        time.sleep(randtime / 100)
        global COUNT
        COUNT+=1

        print("{}: Accepted {} followers.".format(name, COUNT))

    q.get(n)
    print("{}: accepted all followers.".format(name))


def combine():

    q = queue.Queue(200)

    pks = get_list()
    split = splitter(pks, 1)

    while pks!=[]:
        for i in range(len(split)):
            thread = MyThread(q, "Thread-{}".format(i), i, split)
            thread.start()

        while not q.empty():
            pass

        pks=get_list()
        split = splitter(pks, len(split))

    return "Done."