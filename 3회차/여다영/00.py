#00. API 문서와 requests 활용 (연습)

#- 아래의 문서를 활용하여 BTC(비트코인)의 KRW(원) 전일종가를 출력하시오.
#- [https://apidocs.bithumb.com/reference/현재가-정보-조회](https://apidocs.bithumb.com/reference/%ED%98%84%EC%9E%AC%EA%B0%80-%EC%A0%95%EB%B3%B4-%EC%A1%B0%ED%9A%8C)

#결과 예시
#29812000

#pip install -r requirements.txt

#단계
#1.URL로
#2.요청을 보내고
#3.응답을 받는다.

import requests

order_currency = 'BTC'
payment_currency = 'KRW'

URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'

response = requests.get(URL).json()

print(response.get('data').get('prev_closing_price'))