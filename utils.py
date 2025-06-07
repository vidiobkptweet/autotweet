import tweepy
import os
import random
from dotenv import load_dotenv

load_dotenv()

# Inisialisasi koneksi ke Twitter API
def initialize_tweepy():
    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api

# Ambil hashtag trending Indonesia
def get_trending_hashtags(api, woeid=23424846):  # WOEID Indonesia
    try:
        data = api.get_place_trends(id=woeid)
        if not data or "trends" not in data[0]:
            print("Tidak ada data tren.")
            return []
        trends = data[0]["trends"]
        hashtags = [trend["name"] for trend in trends if trend["name"].startswith("#")]
        return hashtags[:3]  # ambil 3 trending hashtag teratas
    except Exception as e:
        print("Gagal ambil hashtag trending:", e)
        return []

# Kirim tweet
def post_tweet(api, content):
    hashtags = get_trending_hashtags(api)
    hashtag_str = ' '.join(hashtags)
    tweet = f"{content}\n\n{hashtag_str}"
    try:
        api.update_status(tweet)
        print("✅ Tweet terkirim:\n", tweet)
    except Exception as e:
        print("❌ Gagal kirim tweet:", e)

# Pilih tweet acak dari file dan kirim
def send_random_tweet():
    api = initialize_tweepy()
    tweets_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'tweets.txt')
    try:
        with open(tweets_path, 'r') as file:
            lines = file.readlines()
            if not lines:
                print("File tweets.txt kosong.")
                return
            tweet_text = random.choice(lines).strip()
            post_tweet(api, tweet_text)
    except FileNotFoundError:
        print(f"File tidak ditemukan: {tweets_path}")
