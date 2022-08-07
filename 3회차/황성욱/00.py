import requests


order_currency = 'BTC'
payment_currency = 'KRW'

headers = {"Accept": "application/json"}

url = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'

response = requests.get(url, headers=headers).json()
print(response.get('data').get('closing_price'))