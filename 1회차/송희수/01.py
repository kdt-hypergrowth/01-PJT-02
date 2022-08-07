import requests
from pprint import pprint

def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
    Base_URL ='https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
    'api_key': 'ae8388bc3e6c351e220eb9a018290351'
    }
    response = requests.get(Base_URL+path, params=params).json()

    return len(response["results"])
    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
