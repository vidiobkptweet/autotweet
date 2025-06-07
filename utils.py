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

def get_trending_hashtags(api, woeid=23424846):  # 23424846 = Indonesia
    try:
        data = api.get_place_trends(id=woeid)
        if not data or "trends" not in data[0]:
            print("Tidak ada data tren yang valid")
            return []
        
        trends = data[0]["trends"]
        hashtags = [trend["name"] for trend in trends if trend["name"].startswith("#")]
        return hashtags[:3]  # Ambil 3 teratas misalnya
    except Exception as e:
        print("Gagal mendapatkan trending hashtags:", e)
        return []

def post_tweet(api, content):
    hashtags = get_trending_hashtags(api)
    hashtag_str = ' '.join(hashtags)
    tweet_with_hashtags = f"{content}\n\n{hashtag_str}"
    api.update_status(tweet_with_hashtags)
    print("Tweet dikirim:", tweet_with_hashtags)

def send_random_tweet():
    api, _ = initialize_tweepy()
    with open(os.path.join(os.path.dirname(__file__), '..', 'data', 'tweets.txt'), 'r') as file:
        lines = file.readlines()
        tweet_text = random.choice(lines).strip()
        post_tweet(api, tweet_text)


send_random_tweet()
