import requests

order_currency = 'BTC'
payment_currency = 'KRW'

URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'

response = requests.get(URL)                        # response에 URL을 불러옴
response2 = response.json()                         # response2에 URL의 정보를 json형식으로 불러옴
response3 = response2.get('data')                   # response3에 URL의 json에서 큰 딕셔너리중에서 data{}를  넣음
response4 = response3.get('prev_closing_price')     # response4에 위에서 가져온 data{}중에서 prev_closing_price를 넣음

print(response4)

