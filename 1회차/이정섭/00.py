import requests

order_currency = 'BTC'
payment_currency = 'KRW'

URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'

response = requests.get(URL).json()
coins = response.get('data')

for coin in coins:
    if coin == 'date':
        continue
    print(coin, coins.get(coin).get('closing_price'))
    