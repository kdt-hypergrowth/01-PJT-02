import requests

order_currency = 'BTC'
payment_currency = 'KRW'
url = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'

response = requests.get(url)

print(response.json().get('data').get('prev_closing_price'))