# API 문서와 requests 활용 

import requests

order_currency = 'BTC'
payment_currency = 'KRW'
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'
response = requests.get(URL)

print(response, type(response)) # <class 'requests.models.Response'>
print(response.json(), type(response.json())) # <class 'dict'>

print('==============================================')

data = response.json()
print(data.get('data').get('prev_closing_price'))  #29812000