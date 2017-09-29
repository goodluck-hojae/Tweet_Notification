from bs4 import BeautifulSoup
import requests

coinmarketcap = requests.get('https://coinmarketcap.com/2')

data = coinmarketcap.text

soup = BeautifulSoup(data,'html.parser')

# retrieve coin name
coin_set = set()
for link in soup.find_all('a'):
    if link.get('href') is not None and "/currencies/" in link.get('href'):
        coin_set.add(link.get('href').split('/')[2])

# retrieve coin twitter name

coin_tweet_set = set()
for coin in coin_set:
    coinmarketcap_social = requests.get('https://coinmarketcap.com/currencies/'+coin+'/#social')
    data_social = coinmarketcap_social.text
    soup_social = BeautifulSoup(data_social,'html.parser')

    for link in soup_social.find_all('a'):
        if link.get('href') is not None and "twitter" in link.get('href'):
            if link.string.split('@')[1] != 'CoinMKTCap':
                coin_tweet_set.add(link.string.split('@')[1])
                print(link.string.split('@')[1])

print(coin_tweet_set)