import time
import random
from Bots.Functions.API import login

api = login.login()

try:
    api = login.login()
    time.sleep(20)
except:
    api=login.login()

unf_list = open("unf.txt", "a")


def get_list(username):

    name = api.username_info(username)

    id = name["user"]["pk"]

    rank_token = api.generate_uuid()

    f_list = api.user_following(id, rank_token)

    return f_list


def unfollow_script(username, no_check):
    list = get_list(username)
    self_time = api.username_feed(username)["items"][0]["taken_at"]
    count=0


    for i in range(len(list["users"])):
        rand = random.randint(1, 10)
        o_user = list["users"][i]["username"]
        o_user_id = list["users"][i]["pk"]
        if len(api.username_feed(o_user)["items"]) > 0:
            last_post = api.username_feed(o_user)["items"][0]
            o_time=last_post["taken_at"]
            if (self_time-o_time) >= 5256000.0 and o_user not in no_check:
                api.friendships_destroy(o_user_id)
                print("Unfollowed {}.".format(o_user))
                unf_list.write("{}\n".format(o_user))
                count+=1
            else:
                print("{} is fine.".format(o_user))
        time.sleep(rand/10)
    print("Unfollow {} users.".format(count))

