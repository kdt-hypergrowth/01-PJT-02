# 요청 보내고 응답받는 걸 파이썬 내장 함수를 써도 되는데 requests가 편하다. 그래서, pip install requests를 한다.
import requests
# URL로 요청을 보내서 응답 받은 값을 가져온다.
order_currency = 'BTC'
payment_currency = 'KRW'
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'
Response = requests.get(URL)
# print(Response) # <Response [200]> <class 'requests.models.Response'>
# 객체에서 중요한 2가지, 속성과 메서드

# # 속성 예시
# print(Response.status_code) # 200
# print(Response.text, type(Response.text)) # 문자열
# # 메서드 예시
# print(Response.json(), type(Response.json())) # <class 'dict'>

data = Response.json()
# print(data.keys())
# print(data.get('data'))
print(data.get('data').get('prev_closing_price')) # data.get() 자체가 또 딕셔너리라서 get을 쓸 수 있는 것!

