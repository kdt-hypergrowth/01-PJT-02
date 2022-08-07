# API 문서와 requests 활용(연습)
# BTC(비트코인)의 KRW(원) 전일종가 출력

import requests

order_currency = 'BTC'
payment_currency = 'KRW'
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'

response = requests.get(URL)
data = response.json()

print(data.get('data').get('prev_closing_price'))
