# ## 00. API 문서와 requests 활용 (연습)

# - 아래의 문서를 활용하여 BTC(비트코인)의 KRW(원) 전일종가를 출력하시오.

# import requests

# def get_btc_krw():
#     order_currency = "BTC"
#     payment_currency = "KRW"
#     url = f"https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}"

#     res = requests.get(url=url).json()
#     data = res["data"]
#     prev_closing_price = data["prev_closing_price"]

#     return prev_closing_price

# if __name__ == "__main__":
#     print(get_btc_krw())

import requests

order_currency = 'BTC'
payment_currency = 'KRW'
url = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'

response = requests.get(url)

print(response.json().get('data').get('prev_closing_price'))
# 요청을 보내서
# response = requests.get(URL)
# # 응답 받은 값을 가져온다.
# print(response, type(response)) # <response [200]> <class 'requests.models.Response'>

# # 속성 예시
# print(response.status_code) # 200
# print(response.text, type(response.text)) # 문자열

# # 메서드 예시
# # .json() 텍스트 형식의 JSON 파일을 파이썬 데이터 타입으로 변경!
# print(response.json(), type(response.json())) # <class 'dict'>

# print('===========================')

# data = response.json()
# print(data.get('data').get('closing_price'))
# coins : 딕셔너리임
# key : coin 이름
# value : 딕셔너리(코인의 정보)
# for coin in coins:
    # coins.get(coin) <- 코인의 정보인 딕셔너리
    #그 딕셔너리의 closing price
    # print(coin, coins.get(coin).get('closing_price'))
