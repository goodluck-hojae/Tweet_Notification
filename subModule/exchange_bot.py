import requests
import json
import _thread
import time
import sys
import telepot
from googletrans import Translator


TOKEN = '311962567:AAGzqgnoQrAsYpqB6lKHW5Rns9YsupyLp0s' #sys.argv[1]  # get token from command-line
print(TOKEN)
teleBot = telepot.Bot(TOKEN)
translator = Translator()


def getExchangeInfo():
    html = requests.request('get','https://coindar.org/api/v1/lastEvents?limit=1')

    coindar_content = json.loads(html.content.decode('UTF-8'))[0]
    public_date = coindar_content['public_date']
    coin_name = coindar_content['coin_name']
    coin_symbol = coindar_content['coin_symbol']
    caption = coindar_content['caption']
    target_date = str(coindar_content['year']) + '-' + str(coindar_content['month']) + '-' + str(coindar_content['day'])
    proof = coindar_content['proof']

    result = '<< 거래소 관련 소식 - ' + public_date[:10] + '>>' +'\n' \
        + coin_name + '(' + coin_symbol + ') '+ caption + ' (' + target_date +')' +'\n' \
        + proof

    return result

# Telegram Send Messagedd
def sendToTelebot(prev):
        tele_users = teleBot.getUpdates(offset=100000001)
        tele_userid_set = set()
        text = getExchangeInfo()

        try:
            if prev != text:
                for tele_user in tele_users:
                    tele_userid_set.add(tele_user['message']['chat']['id'])

                lang = translator.detect(text).lang

                # en -> ko & ko -> en
                if lang == 'en':
                    print(translator.translate(text, dest='ko').text)
                    tweet = translator.translate(text, dest='ko').text+'\n\n'+text
                else:
                    print(translator.translate(text, dest='en').text)
                    tweet = text + '\n\n' + translator.translate(text, dest='en').text
                teleBot.sendMessage(chat_id=436399842, text='%s' % tweet)
                #teleBot.sendMessage(chat_id=436399842, text='%s' % tweet) #test bot
        except telepot.exception.BotWasBlockedError as e:
            print(e)
        return text

def main():
    prev = ''
    while True:
        prev = sendToTelebot(prev)
        time.sleep(3)

_thread.start_new_thread(main,())

while True:
    time.sleep(10)