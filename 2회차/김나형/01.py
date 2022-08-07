# 01. 인기 영화 조회
# - 인기 영화 목록의 개수를 출력합니다.
# - requests 라이브러리를 활용하여 TMDB에서 현재 인기 있는 영화 목록(Get Populations) 데이터를 요청합니다.
# - 응답 받은 데이터 영화 개수를 반환하는 함수를 작성합니다.
# https://api.themoviedb.org/3/movie/550?api_key=ee778b1a58aeccbc4b3b0e358cb43716

import requests
from pprint import pprint


def popular_count():
    pass 
    # 여기에 코드를 작성합니다.
    
    URL = f'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key' : 'ee778b1a58aeccbc4b3b0e358cb43716',
        'language' : 'ko-KR'
    }
    response = requests.get(URL+path, params=params).json()
    pprint(response)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
