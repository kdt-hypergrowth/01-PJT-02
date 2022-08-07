from typing import cast
import requests
from pprint import pprint


def credits(title):
    pass 
    try:
        URL = 'https://api.themoviedb.org/3'
        path = '/search/movie'
        params = {
            'api_key': '344b9a7b0867ea18b1b9d6356fb7a1f0',
            'language': 'ko-KR',
            'query': title
        }
        response = requests.get(URL + path, params = params).json()      
        movie_id = response.get('results')[0].get('id')

        main_URL = 'https://api.themoviedb.org/3'
        main_path = f'/movie/{movie_id}/credits'
        params = {
            'api_key': '344b9a7b0867ea18b1b9d6356fb7a1f0',
            'language': 'ko-KR',
        }
        main_response = requests.get(main_URL + main_path, params = params).json()
        cast_list = []
        crew_list = []
        for a in main_response.get('cast'):
            if a.get('cast_id') < 10:
                cast_list.append(a.get('name'))
        for a in main_response.get('crew'):
            if a.get('department') == 'Directing':
                crew_list.append(a.get('name'))

        return {'cast' : cast_list, 'crew' : crew_list}

    except:
        return None

if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
