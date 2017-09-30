
from tweepy import StreamListener
from tweepy import Stream
import TelegramBot
import tweepy
import json


class TwitterListener(StreamListener):
    def __init__(self, twitter_name):
        self.twitter_name = twitter_name

    def on_data(self, data):
        # process stream data here
        #TelegramBot.sendToTelebot(data[0]['text'])
        #TODO REMOVE SPECIAL CHARACTERS
        tweet = json.loads(data)
        try:
            if 'user' in tweet.keys():
                screen_name = tweet['user']['screen_name'].lower()
                print(screen_name + 'is in the list ->' + str(screen_name in self.twitter_name))
                if screen_name in self.twitter_name :
                    # CHECK Retweet
                    if not 'RT' in tweet['text'][:3] and not '@' in tweet['text'][:3] :
                        TelegramBot.sendToTelebot(tweet['user']['name'] + '\n' + tweet['text'])

        except json.decoder.JSONDecodeError as jsonError:
            print(jsonError)

    def on_error(self, status):
        print(status)

