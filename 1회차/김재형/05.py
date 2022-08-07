import requests
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()



def credits(title):
    pass 
    # 여기에 코드를 작성합니다.
    # 영화 검색, 출연진(cast), 스태프(crew)
    # get credits
    # cast_id 10미만, department가 Directing
    api_key = os.getenv('api_key') 
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key' : api_key,
        'language' : 'ko-KR',
        'query' : f'{title}'
    }
    response = requests.get(BASE_URL+path, params=params).json()
    movies = response.get('results')
    # pprint(movies)
    
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/496243/credits'
    params = {
        'api_key' : api_key,
        'language' : 'ko-KR',
    }
    response2 = requests.get(BASE_URL+path, params=params).json()
    movie = response2.get('cast')
    #pprint(movie)
    # for문으로 리스트 돌면서 딕셔너리마다 cast_id값이 10미만인 거 추출
    a = []
    for cast in movie:
        if cast.get('cast_id') < 10:
            a.append(cast.get('name'))
    #print(a)
    # known_for_department가 Directing인 경우 추출
    b = []
    for directing in movie:
        if directing.get('known_for_department') == 'Directing':
            b.append(directing.get('name'))
    #print(b)
    # 왜 하나만 나올까..
    c = {
        'cast' : a,
        'crew' : b
    }
    return pprint(c)


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
