import requests
import json#1
import requests
import json

#API 키 (v3 auth)
#de3d5824ffe66b5d535f7edae4d285d6
#API 요청 예
#https://api.themoviedb.org/3/movie/550?api_key=de3d5824ffe66b5d535f7edae4d285d6
#API 읽기 액세스 토큰 (v4 auth)
#eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkZTNkNTgyNGZmZTY2YjVkNTM1ZjdlZGFlNGQyODVkNiIsInN1YiI6IjYyZGEyNDU0YmJlMWRkMDA1MjliZjYxYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.bLUvLxddYBLNgqLXTFrIijBYf8t2c1tQyWNW-fg-_m4


def popular_count():
    base_url = 'https://api.themoviedb.org/3'
    path = '/movie/popular'

    params = {
        'api_key' : 'de3d5824ffe66b5d535f7edae4d285d6',
        'language' : 'ko',
    }
    res = requests.get(base_url+path, params=params)
    data = res.json()
    result = data['results']
    
    return len(result)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20



def popular_count():
    base_url = 'https://api.themoviedb.org/3'
    path = '/movie/popular'

    params = {
        'api_key' : 'de3d5824ffe66b5d535f7edae4d285d6',
        'language' : 'ko',
    }
    res = requests.get(base_url+path, params=params)
    data = res.json()
    result = data['results']
    
    return len(result)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20

