# e3ebcaf0cb86336e3fa61579f1f0569b
# https://api.themoviedb.org/3/movie/76341?api_key=<<api_key>>
from urllib import response
import requests


def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
    BASE_URL = f'https://api.themoviedb.org/3'
    # 위 사이트에서 정보를 가져올 것이다.
    path = '/movie/popular'
    # 세부항목은 /movie/popular이다
    params = {
        'api_key': 'e3ebcaf0cb86336e3fa61579f1f0569b'
    }
    # 발급받은 api_key 값을 넣어준다

    res = requests.get(BASE_URL+path, params).json()
    # res에 받아올 주소와 형식을 입력해준다.
    results = res['results']
    # key값이 results인 경우의 value 값들을 가져온다


    return len(results) 
    # 필요한 것은 몇 개의 데이터를 가지느냐이므로 항목의 길이를 출력하면 값을 구할 수 있다.

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
