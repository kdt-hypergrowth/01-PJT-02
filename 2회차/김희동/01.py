from itertools import count
import requests
from pprint import pprint

def popular_count():
    pass
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key' : '802f1efe43a0b0e486e74690ed6e97ae', 
        'language' : 'ko-KR'}
    response = requests.get(BASE_URL+path, params=params).json()
    # pprint(response.keys())
    # pprint(response['results'])
    # pprint(len(response['results']))
    return len(response['results'])

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
