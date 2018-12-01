from API.instagram_private_api import Client
import os

dir=os.getcwd()

with open("config.txt") as infile:
    user, password, debug = [line.strip() for _, line in zip(range(3), infile)]


def login():

    api = Client(user, password)
    return api