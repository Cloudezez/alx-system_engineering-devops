#!/usr/bin/python3
import praw

# Replace these with your actual Reddit credentials
CLIENT_ID = 'awmOM8qtNxcAZ3ws2ecmfA'
CLIENT_SECRET = 'cy4i5OLb_0FCgA_O0giSRCIx6tFGvA'
USER_AGENT = 'jaddy:v1.0.0 (by /u/Resident_Juice2510)'

def get_reddit_instance():
    return praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT
    )

def get_subscribers(subreddit):
    reddit = get_reddit_instance()
    try:
        sub = reddit.subreddit(subreddit)
        return sub.subscribers
    except Exception as e:
        print(f"Exception occurred: {e}")
        return 0

def get_top_ten(subreddit):
    reddit = get_reddit_instance()
    try:
        top_posts = reddit.subreddit(subreddit).hot(limit=10)
        return [post.title for post in top_posts]
    except Exception as e:
        print(f"Exception occurred: {e}")
        return ["None"]

