import requests
from pprint import pprint

def credits(title):
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
    'api_key': '8ae2dc747474b46331631d5ccf4f8966',
    'language': 'ko-KR',
    'query': title
    }

    response = requests.get(BASE_URL+path, params=params).json()
    movies = response.get('results')

    if len(movies) == 0:
        return None

    search_movie = movies[0]
    id = search_movie.get('id')

    BASE_URL = 'https://api.themoviedb.org/3'
    path = f'/movie/{id}/credits'
    params = {
    'api_key': '8ae2dc747474b46331631d5ccf4f8966',
    'language': 'ko-KR'
    }        

    credit = requests.get(BASE_URL+path, params=params).json()
    cast = []
    crew = []

    for i in credit.get('cast'):
        if i.get('cast_id') < 10:
            cast.append(i.get('name'))

    for i in credit.get('crew'):
        if i.get('department') == 'Directing':
            crew.append(i.get('name'))

    result = {"cast": cast, "crew": crew}

    return result


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
