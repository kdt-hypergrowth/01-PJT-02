import requests
from pprint import pprint


def credits(title):
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': '',
        'language': 'ko-KR',
        'query': title
    }

    response = requests.get(BASE_URL+path, params=params).json()  
    movies = response.get('results')

    if movies == None:
        return None
    else:
        movie_id = movies[0]['id']

    BASE_URL = 'https://api.themoviedb.org/3'
    path = f'/movie/{movie_id}/credits'
    params = {
        'api_key': '',
        'language': 'ko-KR'
    }

    response = requests.get(BASE_URL+path, params=params).json()  
    cast = response.get('cast')
    crew = response.get('crew')
    re_cast = []
    re_crew = []
    
    for i in cast:
        cast_id = i.get('cast_id')
        if cast_id < 10:
            re_cast.append(i.get('name'))
    
    for j in crew:
        department = j.get('department')
        if department == 'Directing':
            re_crew.append(j.get('name'))

    cast_crew = {"cast" : re_cast, "crew" : re_crew}

    return cast_crew


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
