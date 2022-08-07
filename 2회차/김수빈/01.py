import requests
from pprint import pprint

BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/popular'
params = {
    'api_key': '8ae2dc747474b46331631d5ccf4f8966',
    'language': 'ko-KR'
}

def popular_count():
    response = requests.get(BASE_URL+path, params=params).json()
    return len(response.get('results'))

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
