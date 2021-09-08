import tweepy

from bot import TwitterBot


def filter_tweets():
    """ Filter tweets based on the hashtag """
    hashtag = "#MachineLearning"
    searchword = hashtag + " -filter:retweets"
    tweets = twt.search_hashtags(searchword)
    #print (tweet)

    filter_words = ['free','course','book','eBook']
    text_tweets =[]
    for word in filter_words:
        for tweet in tweets:
            #print (tweet)
            if word in tweet:
                print ("here")
                text_tweets.append(tweet)

    print (text_tweets)

if __name__ == "__main__":
    twt = TwitterBot()
    filter_tweets()

