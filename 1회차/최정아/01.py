# 6113132e8f47d25f160c7567d23869a3
# https://api.themoviedb.org/3/movie/76341?api_key=<<api_key>>
# 요청을 보냄 (request를 사용함)
import requests


def popular_count():
    pass 
    #URL 만듬
    BASE_URL = 'https://api.themoviedb.org/3' 
    # 상세경로에 popular movie 볼 수 있음
    path = '/movie/popular'
    #params에 api_key라고 하는 곳에 값을 넣음
    params = {
        'api_key': '6113132e8f47d25f160c7567d23869a3'
    }
    # 응답결과는 requests.get(BASE_URL에 더하기 path
    # 이것을 JSON으로 바꿔줌
    response = requests.get(BASE_URL+path, params=params).json()
    print(response)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
