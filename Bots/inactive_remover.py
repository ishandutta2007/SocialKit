import time
import random
from Bots.Functions.API import login
from API.instagram_web_api import Client

try:
    api = login.login()
    print("Logged in.\n")
except:
    time.sleep(20)
    api = login.login()

def get_following(username):
    name = api.username_info(username)
    id = name["user"]["pk"]
    rank_token = api.generate_uuid()
    f_list = api.user_following(id, rank_token)

    return f_list


def get_followers(username):

    name = api.username_info(username)
    id = name["user"]["pk"]
    rank_token = api.generate_uuid()
    f_list = api.user_followers(id, rank_token)

    return f_list


def get_likers(username):
    name = api.username_info(username)
    id = name["user"]["pk"]
    rank_token = api.generate_uuid()


def get_inactives(username):
    followers = get_followers(username)
    following = get_following(username)


def remove_script(username, no_check):
    pass

