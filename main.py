from upbit import Upbitpy
import requests
upbit = Upbitpy()
tickers = upbit.get_ticker(['KRW-BTC', 'KRW-EOS'])
for ticker in tickers:
    print('%s trade price : %d' % (ticker['market'], ticker['trade_price']))

# 내 계좌 코인별 잔액
Account_check = upbit.get_accounts()
for coin in Account_check:
    print('%s : %s' %(coin['currency'], coin['balance']))
# KRW-BTC
all_market_all = upbit.get_market_all()
key_value = ['KRW-BTC']
for coin1 in all_market_all:
    if coin1['market'] in key_value:
      print(coin1)

