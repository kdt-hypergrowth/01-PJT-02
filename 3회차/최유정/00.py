# 00. API 문서와 requests 활용 (연습)
# - 아래의 문서를 활용하여 BTC(비트코인)의 KRW(원) 전일종가를 출력하시오.
# - https://apidocs.bithumb.com/reference/현재가-정보-조회 

#pip install -r requestsments.txt
import requests

def get_btc_krw():

#URL로
    order_currency = 'BTC'
    payment_currency = 'KRW'
    URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'

# #요청을 보내서
    response = requests.get(URL).json()#딕셔너리->키로접근
    data = response['data']
    prev_closing_price =  data['prev_closing_price']

    return prev_closing_price

if __name__ == '__main__':
    print(get_btc_krw())

# #응답 받은 값을 가져온다.
# print(response, type(response)) #<Response [200]> <class 'requests.models.Response'>

# #속성 예시
# print(response.status_code) #200
# print(response.text, type(response.text)) #str

# #메서드 예시
# #.json() : 텍스트 형식의 json 파일을 파이썬 데이터 타입으로 변경
# print(response.json(), type(response.json()))#<class 'dict'>



