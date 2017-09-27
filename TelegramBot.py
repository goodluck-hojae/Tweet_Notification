import sys
import telepot

TOKEN = sys.argv[1]  # get token from command-line
print(TOKEN)
teleBot = telepot.Bot(TOKEN)

# Telegram Send Message
def sendToTelebot(tweet):
        tele_users = teleBot.getUpdates(offset=100000001)
        tele_userid_set = set()

        for tele_user in tele_users:
            tele_userid_set.add(tele_user['message']['chat']['id'])
        print(tele_userid_set)

        for tele_userid in tele_userid_set:
            teleBot.sendMessage(tele_userid,tweet)