from API.instagram_private_api import Client

with open("./config.txt") as infile:
    user, password, debug = [line.strip() for _, line in zip(range(3), infile)]

api = Client(user, password)

photo =

