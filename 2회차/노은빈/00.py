import requests
#URL로
URL = f'https://api.bithumb.com/public/ticker/BTC_KRW'
#요청을 보내서
headers = {'Accept': 'application/json'}
response = requests.get(URL,headers = headers)
#응답 받은 값을 가져오기
print(response.text)

data = response.json()
#data는 딕셔너리 key로 접근
print(data.get('data').get('prev_closing_price'))