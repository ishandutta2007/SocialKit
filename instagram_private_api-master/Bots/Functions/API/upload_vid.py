from Bots.Functions.API import login
import base64

api = login.login()


def upload_video(video, W, H, duration, thumbnail, caption):

    with open(video, "rb") as videoFile:
        video_string = base64.b64encode(videoFile.read())

    with open(thumbnail, "rb") as imageFile:
        thumbnail_string = base64.b64encode(imageFile.read())

    api.post_video(video_string, (W, H), duration, thumbnail_string, caption, False,)

