import sys, twitter, tweepy
import time
import _thread


class Bot:
    def __init__(self, keys):
        self._consumer_key = keys[0]
        self._consumer_secret = keys[1]
        self._access_token = keys[2]
        self._access_secret = keys[3]

        try:
            auth = tweepy.OAuthHandler(self._consumer_key,
                                       self._consumer_secret)
            auth.set_access_token(self._access_token, self._access_secret)

            self.client = tweepy.API(auth)
            if not self.client.verify_credentials():
                raise tweepy.TweepError
        except tweepy.TweepError as e:
            print('ERROR : connection failed. Check your OAuth keys.')
        else:
            print('Connected as @{}, you can start to tweet !'.format(self.client.me().screen_name))
            self.client_id = self.client.me().id


    def get_last_tweet(self,my_string):
        prev_tweet = None
        while True:
            tweet = self.client.user_timeline(id = self.client_id, count = 1)[0]
            if prev_tweet != tweet.text:
                print(tweet.id)
                print(tweet.text)
                prev_tweet = tweet.text
            # AttributeError: 'ResultSet' object has no attribute 'text'
            time.sleep(10)

consumer_key = 'W26NNy6uylLp3mxqnV7cn8Qqz'
consumer_secret = '8sn8M4PGfMO8Xt1SYPCWyTVVWhHrhvl6LmTCXZKur641wKR9Ia'
access_token_key = '912715351355383808-OwpvxPRotKpCSUf9CprZrnsiBtUGPnG'
access_token_secret = 'b89R6GNbPnrYIV4lbDOs0eRgqnJerEczyMQckyc75ONGF'

keys = [consumer_key, consumer_secret, access_token_key, access_token_secret]

tweetBot = Bot(keys=keys)
_thread.start_new_thread(tweetBot.get_last_tweet,('get_last_tweet',))

while True:
    time.sleep(10)