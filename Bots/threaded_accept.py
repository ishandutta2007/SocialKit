import time
import random
import queue
import threading
from Bots.Functions.API import login


api = login.login()


class MyThread(threading.Thread):
    def __init__(self, tid, name, n, lst):
        threading.Thread.__init__(self)
        self.lst = lst
        self.name = name
        self.n = n
        self.id = tid

    def run(self):
        print("Starting {}".format(self.name))
        accept(self.name, self.n, self.lst)
        print("Exiting {}".format(self.name))



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


def accept(name, n, lst):
    for i in range(len(lst[n])):
        randtime = random.randint(1, 10)
        randtime = randtime / 10
        api.approve(lst[n][i])
        time.sleep(randtime / 100)
    print("{}: accepted all followers.".format(name))

def combine():

    queuelock = threading.Lock()
    workqueue = queue.Queue(20)
    threads = []
    tid=1


    pks = get_list()
    split = splitter(pks, 20)

    while pks!=[]:
        for i in range(20):
            thread = MyThread(tid, "Thread-{}".format(i), i, split)
            thread.start()
            threads.append(thread)
            tid+=1

        queuelock.acquire()
        for i in range(20):
            workqueue.put(i)
        queuelock.release()

        while not workqueue.empty():
            pass

        for t in threads:
            t.join()

        pks=get_list()
        split = splitter(pks, 20)

    return "Done."









