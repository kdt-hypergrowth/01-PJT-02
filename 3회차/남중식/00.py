import requests

# url 설정
url = "https://api.bithumb.com/public/ticker/BTC_KRW"

headers = {"Accept": "application/json"}

# requests의 get 메서드를 통해 응답을 가져옴
response = requests.get(url, headers=headers)

# 입력 받은 json 형식의 str 데이터를 파이썬 데이터 타입으로 변환
data = response.json()

# get 메서드를 통해 접근
print(data.get('data').get('prev_closing_price'))

