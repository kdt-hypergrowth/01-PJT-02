import requests

url = "https://api.bithumb.com/public/ticker/BTC_KRW"

headers = {"Accept": "application/json"}

response = requests.get(url, headers=headers)

data = response.json()

# data는 딕셔너리로, key로 접근
# get을 통해 key값에 접근하면 value값을 출력 가능
print(data.get('data').get('prev_closing_price'))
