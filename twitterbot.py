from keys import consumer_key,consumer_secret,access_token,access_secret
import tweepy


oauth = tweepy.OAuthHandler(consumer_key, consumer_secret)
oauth.set_access_token(access_token, access_secret)
api = tweepy.API(oauth)


def tweet_status():
    message = input("Whats's Happening?......tweet here....")
    api.update_status(message)

def public_tweet():
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)


#tweet_status()
public_tweet()