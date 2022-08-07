import requests
from pprint import pprint


def credits(title):
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': '238bc3228df973eb1c16fa9c8a4a18bc',
        'query': title
    }
    response = requests.get(BASE_URL+path, params=params).json()

    movie = response['results']
    movie_id = 0
    for m in movie:
        movie_id = m['id']
        break
    if movie_id == 0:
        return(None)

    BASE_URL = 'https://api.themoviedb.org/3'
    path = f'/movie/{movie_id}/credits'
    params = {
        'api_key': '238bc3228df973eb1c16fa9c8a4a18bc',
        'language': 'ko-KR'
    }
    response = requests.get(BASE_URL+path, params=params).json()

    movie = response['cast']
    c_list = []
    for c in movie:
        if c['cast_id'] < 10:
            c_list.append(c['name'])

    movie = response['crew']
    d_list = []
    for d in movie:
        if d['department'] == 'Directing':
            d_list.append(d['name'])

    p = {"cast" : c_list, "crew" : d_list}
    return(p)


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
