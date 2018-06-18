from keys import consumer_key,consumer_secret,access_token,access_secret
import tweepy


oauth = tweepy.OAuthHandler(consumer_key, consumer_secret)
oauth.set_access_token(access_token, access_secret)
api = tweepy.API(oauth)


def tweet_status():
    message = input("Whats's Happening?......tweet here....")
    api.update_status(message)

tweet_status()