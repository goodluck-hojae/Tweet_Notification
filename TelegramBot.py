import sys
import telepot
from googletrans import Translator

#TOKEN = '445532097:AAGhyO8zh_cBb9I0bvd1Dj2bCH4DJEzUtOI' #TEST TOKEN
TOKEN = '347870649:AAF2ZfpdDTjssV7mMwJifC3tIfD_gBDUwuU' #sys.argv[1]  # get token from command-line
print(TOKEN)
teleBot = telepot.Bot(TOKEN)
teleBot_en = telepot.Bot('452986802:AAE_zK5iOluBMTpYfEe1L-C8kSTcKkpRr0I')
translator = Translator()

# Telegram Send Messagedd
def sendToTelebot(tweet):
        '''
        tele_users = teleBot.getUpdates(offset=100000001)
        tele_userid_set = set()
        try:
            for tele_user in tele_users:
                tele_userid_set.add(tele_user['message']['chat']['id'])
        '''
        try:
            lang = translator.detect(tweet).lang

            teleBot_en.sendMessage(chat_id=-1001125385910, text='%s' % tweet)
            # en -> ko & ko -> en
            if lang == 'en':
                print(translator.translate(tweet, dest='ko').text)
                tweet = translator.translate(tweet, dest='ko').text+'\n\n'+tweet
            else:
                print(translator.translate(tweet, dest='en').text)
                tweet = tweet + '\n\n' + translator.translate(tweet, dest='en').text
            teleBot.sendMessage(chat_id=-1001125345764, text='%s' % tweet)
            #teleBot.sendMessage(chat_id=436399842, text='%s' % tweet) #test bot
        except telepot.exception.BotWasBlockedError as e:
            print(e)
