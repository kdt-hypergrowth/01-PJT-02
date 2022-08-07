import requests
import json
order_currency = 'BTC'
payment_currency = 'KRW'
url=f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'
response = requests.get(url)

print(response.json()['data']['closing_price'])