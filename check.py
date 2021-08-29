import tweepy
from datetime import datetime

from credentials import *



# Authenticate to Twitter
auth = tweepy.OAuthHandler(API_key, API_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
user = api.get_user('Aqsa_M1')
print(user.followers_count)
print(user.screen_name)
#print(combined_list)
#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)
#api.update_status("harrybot: First tweet!!")
try:
    api.verify_credentials()
    print("Authentication Successful")
    t = datetime.now().hour
    print(t)
    if t == 17:
        print ("true")
        api.update_status("bobthebot: First tweet!!")
except:
        print("Authentication Error")
