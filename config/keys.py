import os
import tweepy

API_KEY = os.environ['KQ9Lq80TDV9mYba6xa3qwYYAq']
API_SECRET = os.environ['RPMd7WK16eiYLv9pj6BDTW0hWvANYJ5bDYl5n82fXad7D2TkdV']
ACCESS_TOKEN = os.environ['1931122807867613184-EezLYRrQ7lmkrpdMV0OqV0bEcbVcWK']
ACCESS_SECRET = os.environ['PWCrven42c7OMXvPm5tcNNlSjsFk0TbYt7rYY8DyCXYU7']

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

# Contoh tweet
api.update_status("Halo dunia dari GitHub Actions 🚀")
