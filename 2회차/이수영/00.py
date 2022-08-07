import requests

order_currency = 'BTC'  # 필요한 코인 이름 하나일때는 이름을 전부일때는 'ALL'
payment_currency = 'KRW'
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'
# URL 불러오기
response = requests.get(URL).json()
# 리퀘스트를 제이슨 형식으로 리스폰스로 저장

print(response.get('data').get('prev_closing_price'))
# 리스폰스 데이터 안에 전일 종가 딕셔너리 가져와서 프린트