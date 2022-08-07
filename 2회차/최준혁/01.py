import requests
from pprint import pprint

# 9917f46b6425e1df8108a68c4d9202b0
def popular_count():
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': '9917f46b6425e1df8108a68c4d9202b0',
        'language': 'ko-KR',
    }

    response = requests.get(BASE_URL+path, params=params).json()
    cnt = 0
    for i in response.get('results'):
        cnt += 1

    return cnt


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
