
from tweepy import StreamListener
from tweepy import Stream
import tweepy
import json
import TwitterListener

consumer_key = '5z0sfk6FYOa6HQwsW50o2rcTc'
consumer_secret = 'uSf6mPLhqVew9QyWsFUp8N6cUEpBDRNwrU48hRpsMrJzOId7UK'
access_token_key = '912715351355383808-ExBFy5wIibRYYuKnjGRarHtzNxXPPnG'
access_token_secret = 'p4VlHmYZwSSUNakbUVz4xU0qrqdX8Vo2EkWXMMu7jkmfR'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
if __name__ == '__main__':

    twitter_name_id_file = open('twitter_name_id')
    id_list = []

    # allowed twitter name
    twitter_name = set()

    # adding twitter list
    for x in twitter_name_id_file.readlines():
        twitter, id = x.split()
        twitter_name.add(twitter.lower())
        id_list.append(id)

    twitterListener = TwitterListener.TwitterListener(twitter_name)
    twitterStream = Stream(auth, twitterListener)
    twitterStream.filter(follow=id_list[:len(twitter_name)])