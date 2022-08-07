import requests

# 아래의 문서를 활용하여 BTC(비트코인)의 KRW(원) 전일종가를 출력하시오. 

def get_btc_krw():
    order_currency = "BTC"
    payment_currency = "KRW"
    url = f"https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}"

    # {'status': '0000', 'data': {'opening_price': '29813000', 'closing_price': '30879000', 
    # 'min_price': '29738000', 'max_price': '30930000', 'units_traded': '4396.18009972', 
    # 'acc_trade_value': '133626653415.0886', 'prev_closing_price': '29812000', 'units_traded_24H': 
    # '5999.63211952', 'acc_trade_value_24H': '181729488129.4528', 'fluctate_24H': '595000', 
    # 'fluctate_rate_24H': '1.96', 'date': '1658483671815'}}
    # print(res)

    # 29812000
    # print(prev_closing_price)

    # 빗썸 url에 json 형태로 api를 request한 데이터 저장
    res = requests.get(url=url).json()
    # res의 'data' 값 저장
    data = res["data"]
    # data의 'prev_closing_price'(전일종가) 저장
    prev_closing_price = data["prev_closing_price"]

    return prev_closing_price


if __name__ == "__main__":
    print(get_btc_krw())