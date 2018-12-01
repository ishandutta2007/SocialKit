from API.instagram_private_api import Client
import base64

with open("./config.txt") as infile:
    user, password, debug = [line.strip() for _, line in zip(range(3), infile)]

api = Client(user, password)

def upload_photo(photo, W:int, H:int, caption:str, location:None, disable_comments:bool):
    with open(photo, "rb") as imageFile:
        byte_string = base64.b64encode(imageFile.read())

    api.post_photo(byte_string, (W, H), caption, None, False, location, disable_comments)




