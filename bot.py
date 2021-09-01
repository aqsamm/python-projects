import tweepy
from datetime import datetime

import credentials
import webscrape


class TwitterBot:

    def __init__(self):
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
        """ returns a cursor object """
        tweets = tweepy.Cursor(self.authenticate().search,
                q=hashtags,result_type='recent').items(100)
        tweet_info = [tweet.text for tweet in tweets]
        return tweet_info

    def check_time(self):
        format = '%H:%M %p'
        datetime.today().strftime(format)

    def post_tweet(self, quote):
        api = self.authenticate()
        user = api.get_user('Aqsa_M1')
        print(user.followers_count)
        print(user.screen_name)
        print(webscrape.combined_list)
        api.update_status(quote)


    def main():
        t = self.check_time()
        quote = random.choice(webscrape.combined_list)
        while True:
            if t == '08:00 AM' or t == '08:01 AM':
                print(t,flush=True)
                self.post_tweet(quote)
                time.sleep(61)
            else:
                t = check_time()
                print(t,flush=True)
                print('It\'s not time yet',flush=True)
                time.sleep(50)


tw=TwitterBot()
#tw.post_tweet("tweepyyttt")
