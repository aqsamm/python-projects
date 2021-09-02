import time
import random

from bot import TwitterBot
import webscrape
import checktime as ct


def main():
    while True:
        t = ct.check_time()
        #print (t)
        quote = random.choice(webscrape.combined_list)
        if t == '22:08 PM' or t == '22:09 PM':
            print(t, flush=True)
            try:
                tw.post_tweet(quote)
                time.sleep(61)
            except twitter.TweepError as error:
                tw.post_tweet(quote)
                time.sleep(61)
        else:
            t = ct.check_time()
            print(t, flush=True)
            print('It\'s not time yet', flush=True)
            time.sleep(50)


if __name__ == "__main__":
    tw=TwitterBot()
    main()
