import time
import random
import tweepy

from bot import TwitterBot
import webscrape
import checktime as ct


def main():
    while True:
        t = ct.check_time()
        #print(t)
        quote = random.choice(webscrape.get_quotes())
        if t == '22:26 PM' or t == '22:27 PM':
            print(t, flush=True)
            try:
                tw.post_tweet(quote)
                time.sleep(61)
            except tweepy.TweepError as error:
                print(error)
                time.sleep(60)

        else:
            t = ct.check_time()
            print(t, flush=True)
            print('It\'s not time yet', flush=True)
            time.sleep(50)


if __name__ == "__main__":
    tw = TwitterBot()
    main()
