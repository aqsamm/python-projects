import tweepy
from datetime import datetime

import credentials
import webscrape


class TwitterBot:

    def __init__(self):
        """ Initialize the credentials """
        self.api_key = credentials.api_key
        self.api_secret_key = credentials.api_secret_key
        self.access_token = credentials.access_token
        self.access_token_secret = credentials.access_token_secret

    def authenticate(self):
        """ Authenticate to Twitter """
        auth = tweepy.OAuthHandler(self.api_key, self.api_secret_key)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)
        return api

    def search_hashtags(self,hashtags):
        """ Returns a cursor object """
        tweets = tweepy.Cursor(self.authenticate().search,
                q=hashtags,result_type='recent').items(100)
        tweet_info = [tweet.text for tweet in tweets]
        return tweet_info

    def post_tweet(self, quote):
        """ Posts tweet on Twitter """
        api = self.authenticate()
        user = api.get_user('Aqsa_M1')
        print(user.followers_count)
        print(user.screen_name)
        #print(webscrape.combined_list)
        api.update_status(quote)

