#아래의 문서를 활용하여 BTC(비트코인)의 KRW(원) 전일종가를 출력하시오. 

import requests

order_currency = 'BTC'
payment_currency = 'KRW'
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'

response = requests.get(URL)

data = response.json()  # data는 클래스가 딕셔너리

print(data.get('data').get('prev_closing_price'))
# data에 있는 전일종가를 추출하자
