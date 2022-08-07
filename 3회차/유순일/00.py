import requests

def get_btc_krw():                                                                          # 빗썸에서 정보 얻어오려고 함수 설정.
    order_currency = "DOGE"                                                                 # coin의 tiker와 구매화폐가 url에 포함되어있고, 
    payment_currency = "KRW"                                                                # coin마다 order, payment 부분이 달지기에 
    url = f"https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}"      # order와 payment를 변수로 설정해줌.

    res = requests.get(url=url).json()                                                      # url에서 json 정보 얻어오기.
    data = res["data"]                                                                      # 얻어온 정보를 리스트하기 위한 코드. 
    prev_closing_price = data["prev_closing_price"]                                         # closing_price만 리스트 할래.

    return prev_closing_price


if __name__ == "__main__":              # 다른 파일에서 import할 때 현재 쓰인 변수와 print값을 불러오지 않게 해주는 코드.    
    print(get_btc_krw())                # 즉, 오롯이 위의 함수만 import 할 수 있게 해줌. __name__과 __main__은 글로벌용어.