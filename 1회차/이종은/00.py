import requests


def get_btc_krw():
    order_currency = "BTC"
    payment_currency = "KRW"
    url = f"https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}"

    res = requests.get(url=url).json()
    data = res["data"] #data는 딕셔너리
    prev_closing_price = data["prev_closing_price"] #데이터 내 전일 종가 출력

    return prev_closing_price #데이터 내 전일 종가 출력 함수 반환


if __name__ == "__main__":
    print(get_btc_krw())