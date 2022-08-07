#전일종가 출력하기

import requests

order_currency = 'BTC'
payment_currency = 'KRW'

url = f"https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}"

res = requests.get(url=url).json()

data = res['data']

prev_closing_price = data['prev_closing_price']

print(prev_closing_price)