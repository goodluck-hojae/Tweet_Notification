import sys
import telepot
from got import Translator
TOKEN = '347870649:AAF2ZfpdDTjssV7mMwJifC3tIfD_gBDUwuU' #sys.argv[1]  # get token from command-line
print(TOKEN)
teleBot = telepot.Bot(TOKEN)
translator = Translator()

# Telegram Send Messagedd
def sendToTelebot(tweet):
        tele_users = teleBot.getUpdates(offset=100000001)
        tele_userid_set = set()
        try:
            for tele_user in tele_users:
                tele_userid_set.add(tele_user['message']['chat']['id'])
            print(translator.translate('hello', dest='ko').text)
            print(translator.translate(tweet, dest='ko').text)
            tweet = translator.translate(tweet, dest='ko').text+'\n\n'+tweet
            teleBot.sendMessage(chat_id=-1001125345764, text='%s' % tweet)
        except telepot.exception.BotWasBlockedError as e:
            print(e)
