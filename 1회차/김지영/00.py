# API 문서와 requests 활용(연습)
# BTC의 KRW 전일 종가 출력하세요
# GET : https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}
# PATH PARAMS = BTC, KRW
# 전일종가 response = prev_closing_price

import requests

order_currency = 'BTC'
payment_currency = 'KRW'
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'
# URL을 통해 order_currency와 payment_currency를 요청해서 response(응답)을 가져온다.
response = requests.get(URL)
print(response,type(response))  # <Response [200]> <class 'requests.models.Response'>

# .json으로 jason파일을 파이썬 데이터타입으로 변경
# print(response.json(), type(response.json()))  # response = {..., 'data' : {..., 'prev_cosing_price' : ~, 
# print('============================================')

data = response.json()
print(data.get('data').get('prev_closing_price')) # 29812000