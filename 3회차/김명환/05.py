import requests
from pprint import pprint


def credits(title):
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': '31d9bb17e9a1cf5696383bf033e42e18',
        'language': 'ko-KR',
        'query': f'{title}'
    }
    response = requests.get(BASE_URL+path, params=params).json().get('results')
   
    if response == []:
        return None
    
    movie_id = response[0]['id']
    
    BASE_URL = 'https://api.themoviedb.org/3'
    path = f'/movie/{movie_id}/credits'
    params = {
        'api_key': '31d9bb17e9a1cf5696383bf033e42e18',
        'language': 'ko-KR',
        'query': f'{title}'
    }
    response = requests.get(BASE_URL+path, params=params).json()
    cast_info = response.get('cast')
    crew_info = response.get('crew')
    
    cast_list = []
    crew_list = []
    
    for cast in cast_info:
        if cast.get('cast_id') < 10:
            cast_list.append(cast.get('name'))
    for crew in crew_info:
        if crew.get('department') == 'Directing':
            crew_list.append(crew.get('name'))
    cast_crew = {}
    cast_crew['cast'] = cast_list
    cast_crew['crew'] = crew_list

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
