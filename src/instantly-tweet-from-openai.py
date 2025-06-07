import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'config'))
import keys
from functions import generate_response, initialize_tweepy, get_formatted_date

prompt = "buatkan saya tweet singkat lucu dengan hashtag #vidiobkp #vidiobokehp dan mention yang lagi trend"
response = generate_response(prompt)

def send_post():
    client, _ = initialize_tweepy()
    tweet_text = f"{response}"
    client.create_tweet(text=tweet_text)
    print("Tweet posted successfully")

send_post()
