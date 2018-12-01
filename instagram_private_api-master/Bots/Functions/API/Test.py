from API.instagram_private_api import Client
from Bots.Functions.API import login


api = login.login()

dick = api.username_info("hrithikhahs")["user"]["pk"]

hrithik = api.username_feed("hrithikhahs")

print(hrithik)