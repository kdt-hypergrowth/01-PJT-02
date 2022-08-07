import requests


order_currency = 'BTC' # BTC COIN 조회
payment_currency = 'KRW' # KRW = 한화로!
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}' # API 불러올 주소

response = requests.get(URL) #requests URL!
data = response.json() # data를 json파일 형식으로 가져옴 (딕셔너리)

print(data.get('data').get('prev_closing_price'))