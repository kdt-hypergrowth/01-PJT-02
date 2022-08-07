import requests
#requests 를 호출해서

order_currency = 'BTC'
payment_currency = 'KRW'
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'
#url 을 설정한뒤

response = requests.get(URL)
#requests를 해당 url로 보낸다

data = response.json()
#response 를 json()형식의
print(data.get('data').get('prev_closing_price'))





