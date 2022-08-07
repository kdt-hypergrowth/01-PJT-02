#31d9bb17e9a1cf5696383bf033e42e18
#https://api.themoviedb.org/3/movie/76341?api_key=<<api_key>>
from urllib import response
import requests
from pprint import pprint

def popular_count():
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': '31d9bb17e9a1cf5696383bf033e42e18',
        'language': 'ko-KR'
    }
    response = requests.get(BASE_URL+path, params=params).json()['results']
   

    return len(response) 

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
