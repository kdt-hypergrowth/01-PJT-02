from unittest import result
from urllib import response
import requests


def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key' : '9ceb4d4268730f0fa5cc90ef67abfc71',
        'language': 'ko-KR'
        }
    response = requests.get(BASE_URL+path, params=params).json().get('results')
    return len(response)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
