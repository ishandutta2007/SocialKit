from API.instagram_private_api import Client
import threading
import time


self_user = str(input("Enter your Instagram username here: "))
self_pass = str(input("Enter your Instagram password here: "))


class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        try:
            check()
        except:
            print("ERROR")

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


def changer():
    api.change_user(o_u, self_email, self_gender)
print("Logged in.")


self_email = api.current_user()["user"]["email"]
self_gender = api.current_user()["user"]["gender"]
c_u = api.current_user()["user"]["username"]
o_u = str(input("Enter the username you wish to change to: "))
t_i = None
got = False
c = 0
wanted = "{'items': [], 'num_results': 0, 'status': 'ok'}"

while not t_i:
    try:
        t_i = int(input("Enter time interval(ms): "))
    except:
        print("Make sure you enter an integer!")




def check():
    global got, o_u, c, wanted
    try:
        ch = str(api.username_info(o_u))
    except:
        got = True
        changer()
        print("Success! Username has been claimed.")
        exit(0)

    c+=1


print("Initiating...")
check()



if got:
    changer()
    print("Success! Username has been claimed.")
    exit(0)


i=0
print("Starting script... press CTRL+C to stop before it gets the name.")
while not got:
    thread = MyThread()
    try:
        thread.start()
        print("RTJ: {} PASSED.".format(c))
    except:
        print("RTJ: {} FAILED.".format(c))
    i+=1
    time.sleep(t_i/1000)

changer()
print("Success! Username has been claimed.")
exit(0)






