

import requests

coin = 'BTC' #찾으려는 목록 주소

payment= 'KRW' # 표기할 값

url = f'https://api.bithumb.com/public/ticker/{coin}_{payment}'


response = requests.get(url)


response.headers['content-type']  #컨텐츠 타입이 무엇인지 확인  #application/json로 나옴 json인걸 알 수 있다.

j =response.json()  # 가져오려는 주소값의 자료를 json으로  가져온다.

print (j.get('data').get('closing_price')) # 제이슨 안의 데이터 키 안에서 클로징프라이스를 키를 통해 가져온다 .



#https://requests.readthedocs.io/en/latest/ 설명