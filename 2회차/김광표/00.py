import requests


def get_btc_krw(): #전일 종가를 불러오는 함수 정의
    order_currency = "BTC" 
    payment_currency = "KRW"
    url = f"https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}"
    res = requests.get(url=url).json() # url로부터 json정보를 요청한다.
    prev_closing_price = res["data"]["prev_closing_price"] #받아온 정보의 data안에 전일종가를 불러온다
    return prev_closing_price


if __name__ == "__main__":
    print(get_btc_krw())