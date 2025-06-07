import os
import random
import requests
from dotenv import load_dotenv
import tweepy

# Load token dari .env
load_dotenv()

# Ambil semua kredensial dari .env
API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET = os.getenv("TWITTER_API_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

# Inisialisasi Tweepy
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def get_trending_hashtags(woeid=23424846):  # WOEID Indonesia
    url = f"https://api.twitter.com/1.1/trends/place.json?id={woeid}"
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
    response = requests.get(url, headers=headers)
    data = response.json()

    trending = []
    for trend in data[0]["trends"]:
        if trend["name"].startswith("#"):
            trending.append(trend["name"])
        if len(trending) >= 3:
            break
    return trending

def post_tweet(content):
    hashtags = get_trending_hashtags()
    hashtag_str = ' '.join(hashtags)
    tweet_with_hashtags = f"{content}\n\n{hashtag_str}"
    api.update_status(tweet_with_hashtags)
    print("Tweet dikirim:", tweet_with_hashtags)

def send_random_tweet():
    with open("data/tweets.txt", "r") as file:
        lines = file.readlines()
        tweet_text = random.choice(lines).strip()
        post_tweet(tweet_text)

send_random_tweet()
