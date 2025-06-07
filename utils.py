import requests
import os

def get_trending_hashtags(woeid=23424846):  # 23424846 = Indonesia
    BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
    url = f"https://api.twitter.com/1.1/trends/place.json?id={woeid}"
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Gagal ambil hashtag trending:", response.text)
        return []
    data = response.json()
    trends = data[0]['trends']
    hashtags = [trend['name'] for trend in trends if trend['name'].startswith('#')]
    return hashtags[:3]  # ambil 3 hashtag teratas
