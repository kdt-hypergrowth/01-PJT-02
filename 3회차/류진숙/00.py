
# 00. API 문서와 requests 활용
# BTC의 KRW 전일종가를 출력

import requests

url = 'https://api.bithumb.com/public/ticker'
btc_info = {
    'BTC' : 'KRW'
}

response = requests.get(url, params=btc_info).json()

print(response.get('data').get('prev_closing_price'))
