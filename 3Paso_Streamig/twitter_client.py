# encoding: utf-8 
# esta libreria seria para usar las llaves de twitter que hemos exportado en la consola o terminal.
import os
import sys
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():

    try:
        consumer_key = 'TWITTER_CONSUMER_KEY'
        consumer_secret = 'TWITTER_CONSUMER_SECRET'
        access_token = 'TWITTER_ACCESS_TOKEN'
        access_secret = 'TWITTER_ACCESS_SECRET'
    except KeyError:
        sys.stderr.write("TWITTER_* no se encuentra las llaves\n")
        sys.exit(1)    
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth

def get_twitter_client():
    auth = get_twitter_auth()
    client = API(auth)
    return client
