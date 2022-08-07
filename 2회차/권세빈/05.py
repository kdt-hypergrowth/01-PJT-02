import requests
from pprint import pprint
from dotenv import load_dotenv
import os
load_dotenv()

def credits(title):
    try:
        URL = 'https://api.themoviedb.org/3'
        path = '/search/movie'
        params = {
            'api_key': os.environ.get('api_key'),
            'language': 'ko-KR',
            'query': title
        }
        response = requests.get(URL+path, params=params).json()
        search = response.get('results')[0].get('id')
        movie_id = search
        URL = 'https://api.themoviedb.org/3'
        path =f'/movie/{movie_id}/credits'
        params = {
            'api_key': '79d21b47771ad41e6e0ed5b1a8b503e7',
            'language': 'ko-KR',
        }
        response = requests.get(URL+path, params=params).json()
        casts = response.get('cast')
        crews = response.get('crew')
        cast = []
        crew = []
        for p in casts:
            if p['cast_id'] < 10:
                cast.append(p['name'])
        for s in crews:
            if s['department'] == 'Directing':
                crew.append(s['name'])
        dict = {
            'cast': cast,
            'crew': crew
        }
        return(dict)
    except:
        pass
    


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
