from cgi import print_arguments
import requests



#함수 설정
def get_btc_krw():
    # URL로 전송
    order = 'BTC'
    paymen = 'KRW'
    url = f"https://api.bithumb.com/public/ticker/{order}_{paymen}"
    # 요청을 보내면서 json 파일로 변환
    response = requests.get(url=url).json()
    # api에 있는 데이터 입력
    data = response["data"]
    # data안에 있는 리스트에서 전일종가를 불러서 변수 선언
    prev_closing_price = data["prev_closing_price"]
    return prev_closing_price

if __name__ == "__main__":
    print(get_btc_krw())