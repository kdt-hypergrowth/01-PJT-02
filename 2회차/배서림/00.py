# 00. API 문서와 requests 활용 (연습)

# 아래의 문서를 활용하여 BTC(비트코인)의 KRW(원) 전일종가를 출력하시오.
# https://apidocs.bithumb.com/reference/현재가-정보-조회


import requests

order_currency = 'BTC'
payment_currency = 'KRW'
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'

response = requests.get(URL)
data = response.json()
print(data.get('data').get('prev_closing_price'))


# output
#29812000