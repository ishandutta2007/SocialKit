from API.instagram_private_api import Client
import base64

with open("./config.txt") as infile:
    user, password, debug = [line.strip() for _, line in zip(range(3), infile)]

api = Client(user, password)

def upload_video(video, W, H, duration, thumbnail, caption, location, disable_comments):

    with open(video, "rb") as videoFile:
        byte_string = base64.b64encode(videoFile.read())

