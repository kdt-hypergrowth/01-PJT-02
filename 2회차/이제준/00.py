# pip install requests 
import requests
# URL로
order_currency = 'BTC' 
payment_currency = 'KRW' 
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'
# 요청을 보내서
response = requests.get(URL)

# print(response.json())  response를 json으로 열기

data = response.json()
print(data.get('data').get('prev_closing_price'))