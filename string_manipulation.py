
bittrex_twitter_list = open('bittrex_twitter_list')
twitter_list = open('twitter_list')

# coinmarketcap
twitter_list_set = twitter_list.readlines()
twitter_list_set = set([twitter.strip('\n') for twitter in twitter_list_set])
#print(twitter_list_set)

# bittrex
bittrex_twitter_list_set = bittrex_twitter_list.readlines()
bittrex_twitter_list_set = set([twitter.strip('\n') for twitter in bittrex_twitter_list_set])
#print(bittrex_twitter_list_set)

bitrrex_set = bittrex_twitter_list_set.difference(twitter_list_set)
for x in bitrrex_set:
    print(x)
