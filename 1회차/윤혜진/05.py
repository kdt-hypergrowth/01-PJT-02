import requests
from pprint import pprint
from dotenv import load_dotenv
import os

def credits(title):
    load_dotenv()
    key = os.environ.get('TMDB_API_key')

    # 1) 검색한 영화를 조회한 후, 첫번째 영화의 id를 가져옴
    base_url = 'https://api.themoviedb.org/3'
    path1 = '/search/movie'
    prameters1 = {
        'api_key' : key,
        'language': 'ko-KR',
        'query':title,
        'page':1
    }
   
    response1 = requests.get(base_url + path1, params=prameters1).json()
    
    # 영화 제목으로 검색해, 찾아준 영화 목록을 출력
    search_rst = response1.get('results')   
    # 검색한 영화 제목이 존재하면, 첫번째 영화의 id값을 기록
    movie_id = 0
    if search_rst:
        movie_id = search_rst[0]['id']
    # 검색한 영화 제목이 존재하지 않으면 반환
    else:
        return None
    


    # 2) 해당 영화에 대한 출연진과 스태프 목록 출력
    path2 = f'/movie/{movie_id}/credits'
    prameters2 = {
        'api_key' : '36e69126e5702e17a95125dc94bbccbe',
        'language': 'ko-KR'
    }
   
    response2 = requests.get(base_url + path2, params=prameters2).json()

    cast_crew_info = {
        'cast':[],
        'crew':[]
    }
    for cast in response2.get('cast'):
        if cast.get('cast_id') < 10:
            cast_crew_info['cast'].append(cast.get('name'))
    
    for crew in response2.get('crew'):
        if crew.get('department') == 'Directing':
            cast_crew_info['crew'].append(crew.get('name'))

    return cast_crew_info




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
