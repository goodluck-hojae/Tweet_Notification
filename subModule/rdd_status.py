
import ccxt

def rdd_status():
    bittrex   = ccxt.bittrex()
    bittrex.load_markets()
    rdd_asks_price = bittrex.fetch_order_book(bittrex.symbols[178])['asks'][0][0]
    rdd_asks_number = bittrex.fetch_order_book(bittrex.symbols[178])['asks'][0][1]
    rdd_bids_price = bittrex.fetch_order_book(bittrex.symbols[178])['bids'][0][0]
    rdd_bids_number = bittrex.fetch_order_book(bittrex.symbols[178])['bids'][0][1]
    msg = 'rdd ask price : '+ str(rdd_asks_price) + ' remaining asks(BTC) -> ' + str(rdd_asks_price *
                                                                                     rdd_asks_number)+'\n'\
          +'rdd bid price : ' + str(rdd_bids_price) + ' remaining bids(BTC) -> ' + str(rdd_bids_price * rdd_bids_number)
    return msg, rdd_asks_number, rdd_bids_number
