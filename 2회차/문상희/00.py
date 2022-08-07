# requests 모듈 설치
import requests

# A1.
# 가져올 URL정보
# order_currency = 'BTC' 
# payment_currency = 'KRW' 
# URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'
# # URL값을 가져옴.
# response = requests.get(URL)
# # 원하는 값 출력
# print(response.json().get('data').get('prev_closing_price'))
        #1           #2             #3

        #1 가져온 URL json으로 보여줌
        #  {'status': '0000', 'data': {'opening_price': '29813000', 'closing_price': '30185000', 'min_price': '29738000', 'max_price': '30680000', 'units_traded': '3203.79350938', 'acc_trade_value': '97192568940.434', 'prev_closing_price': '29812000', 'units_traded_24H': '6176.51460041', 'acc_trade_value_24H': '186590198378.1478', 'fluctate_24H': '178000', 'fluctate_rate_24H': '0.59', 'date': '1658463254686'}}

        #2 딕셔너리 키 값이 data인 값을 보여줌
        #  {'opening_price': '29813000', 'closing_price': '30183000', 'min_price': '29738000', 'max_price': 
        # '30680000', 'units_traded': '3206.53460938', 'acc_trade_value': '97275297972.934', 'prev_closing_price': '29812000', 'units_traded_24H': '6173.72679664', 'acc_trade_value_24H': '186506941596.2799', 'fluctate_24H': '159000', 'fluctate_rate_24H': '0.53', 'date': '1658463320562'}

        #3 data 값 안에서 전일종가를 뜻하는 키 prev_closing_price에 부합하는 밸류 출력


# A2.

def p_c_p():
    url = f"https://api.bithumb.com/public/ticker/BTC_KRW"

    res = requests.get(url).json()                          #
    data = res['data']
    prev_closing_price = data['prev_closing_price']

    return prev_closing_price

if __name__ == "__main__":
    print(p_c_p())