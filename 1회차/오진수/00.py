#BTC(비트코인)의 KRW(원) 전일종가 29812000

from sqlite3 import DatabaseError
import requests

order_currency = 'BTC'
payment_currency = 'KRW'
url = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'

response = requests.get(url)
print(response)

data = response.json()
print(data.get('data').get('prev_closing_price'))
      #data.get('data)자체가 딕셔너리