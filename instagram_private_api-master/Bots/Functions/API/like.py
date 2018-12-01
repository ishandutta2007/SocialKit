from Bots.Functions.API import login

api = login.login()


def like(username, post_number):
    post_id = api.username_feed(username)["items"][post_number-1]["id"]
    api.post_like(post_id)

