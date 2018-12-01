from Bots.Functions.API import login
import base64

api = login.login()


def upload_photo(photo, W:int, H:int, caption:str):
    with open(photo, "rb") as imageFile:
        byte_string = base64.b64encode(imageFile.read())

    api.post_photo(byte_string, (W, H), caption, None, False)




