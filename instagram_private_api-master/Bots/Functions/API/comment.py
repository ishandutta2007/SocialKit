from Bots.Functions.API import login

api = login.login()

def comment(username, post_number, text):
    post_id = api.username_feed(username)["items"][post_number-1]["id"]
    api.post_comment(post_id, text)