# 문제00. BTC(비트코인)의 KRW(원) 전일종가를 출력

# requests 모듈을 가져옴
import requests

# 변수 선언 및 접속 URL 설정
order_currency = 'BTC' # 주문 통화 변수
payment_currency = 'KRW' # 결제 통화 변수

URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'

# 요청 보내서 응답을 받음
response = requests.get(URL)

# 응답 받은 데이터(json)을 가져옴
data = response.json()

# 가져온 json의 딕셔너리 형태를 확인하였을 때, 'data'라는 key에 다시 딕셔너리 형태가 들어가있음.
# 그래서 'data'값을 get하고, 그 data 안에 다시 전일종가 변수인 prev_closing_price를 get함.
print('BTC 전일 종가:', data.get('data').get('prev_closing_price'))