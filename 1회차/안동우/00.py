from urllib import response
import requests
order_currency= 'ALL'
payment_currency= 'KRW'

c = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'

a = requests.get(c).json()
b = a.get('data')


for coin in b:

    if coin == 'date':
        continue
    print(coin, b.get(coin).get('closing_price'))