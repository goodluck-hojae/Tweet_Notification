
from tweepy import StreamListener
from tweepy import Stream
import tweepy
import TelegramBot
import json

consumer_key = '5z0sfk6FYOa6HQwsW50o2rcTc'
consumer_secret = 'uSf6mPLhqVew9QyWsFUp8N6cUEpBDRNwrU48hRpsMrJzOId7UK'
access_token_key = '912715351355383808-ExBFy5wIibRYYuKnjGRarHtzNxXPPnG'
access_token_secret = 'p4VlHmYZwSSUNakbUVz4xU0qrqdX8Vo2EkWXMMu7jkmfR'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)
twitter_name = set()
class StdOutListener(StreamListener):

    def on_data(self, data):
        # process stream data here
        #TelegramBot.sendToTelebot(data[0]['text'])
        #TODO REMOVE SPECIAL CHARACTERS
        tweet = json.loads(data)
        try:
            if 'user' in tweet.keys():
                print('[user][screenname] ' + tweet['user']['screen_name'] )
                print('check in the twitter list ' + str(tweet['user']['screen_name'].lower() in twitter_name))
                print(tweet['user']['screen_name'].lower() in twitter_name)
                print('test')
                if tweet['user']['screen_name'].lower() in twitter_name :
                    print('RT in tweet[text] ' + str('RT' in tweet['text']))
                    print(tweet['text'])
                    if not 'RT' in tweet['text'][:3] and not '@' in tweet['text'][:3] :
                        TelegramBot.sendToTelebot(tweet['user']['name'] + '\n' + tweet['text'])
        except json.decoder.JSONDecodeError:
            print('json.decoder.JSONDecodeError')
    def on_error(self, status):
        print(status)

if __name__ == '__main__':

    file = open('twitter_id')
    list = []
    list.append('912715351355383808')
    twitter_name.add('dr_coder_kor')
    for x in file.readlines():
        twitter, id = x.split()
        twitter_name.add(twitter.lower())
        list.append(id)
    listener = StdOutListener()
    twitterStream = Stream(auth, listener)
    twitterStream.filter(follow=list[:186])