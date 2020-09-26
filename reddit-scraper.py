from dotenv import load_dotenv
import os
import praw

load_dotenv(verbose=True)

reddit = praw.Reddit(
        client_id = os.getenv("CLIENT_ID"),
        client_secret = os.getenv("CLIENT_SECRET"),
        password = os.getenv("R_PASSWORD"),
        username = os.getenv("R_USERNAME"),
        user_agent="wow shitpost bot"
)


print(reddit.user.me())
