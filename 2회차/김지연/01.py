from urllib import response
import requests
# 3eab28de576c4bc938a81c1a00382b8a
# /movie/popular
# https://api.themoviedb.org/3/movie/76341?api_key=<<api_key>>

def popular_count():
    BASE_URL = 'https://api.themoviedb.org/3/'
    path = 'movie/popular'
    params = {
        'api_key': '3eab28de576c4bc938a81c1a00382b8a',
        'language': 'ko-KR' # 한국어
    }

    response = requests.get(BASE_URL+path, params=params).json()
    print(response)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
