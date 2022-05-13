import ccxt

print(ccxt.exchanges)

kucoin = ccxt.kucoin()
okex = ccxt.okex()
bitmex = ccxt.bitmex()
huobipro = ccxt.huobipro()

exchange_id = 'binance'
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class()

symbol = 'BTC/USDT'
timeframe = '1h'

binance_ohlcv = exchange.fetch_ohlcv(symbol, timeframe)
kucoin_ohlcv = kucoin.fetch_ohlcv(symbol, timeframe)
okex_ohlcv = okex.fetch_ohlcv(symbol, timeframe)
huobipro_ohlcv = huobipro.fetch_ohlcv(symbol, timeframe)

print('\nBinance Data Format: \n')
print(binance_ohlcv[0])
print('\Kucoin Data Format: \n')
print(kucoin_ohlcv[0])
print('\Okex Data Format: \n')
print(okex_ohlcv[0])
print('\nHuobipro Data Format: \n')
print(huobipro_ohlcv[0])

print('\nDefault number of candles: \nBinance: {} \nKucoin: {} \nOkex: {} \nHuobipro: {}'.format(
    len(binance_ohlcv), len(kucoin_ohlcv), len(okex_ohlcv), len(huobipro_ohlcv)))
