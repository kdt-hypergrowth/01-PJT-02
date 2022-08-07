from http.client import PAYMENT_REQUIRED
import requests

order_currency = 'BTC'
payment_currency ='KRW'
URL =  f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'
response = requests.get(URL).json()
result = response.get('data').get('prev_closing_price')
print(result) 