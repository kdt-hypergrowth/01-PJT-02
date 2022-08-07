from sqlite3 import paramstyle
from tkinter.messagebox import NO
from xml.sax import default_parser_list
import requests
from pprint import pprint


def credits(title):

    base_url = 'https://api.themoviedb.org/3/search/movie'
    params = {
        'api_key': 'f25f9449dadd6f959e63b7b058966cea',
        'language': 'ko-KR',
        'query' : title
    }
    de_params = {
        'api_key': 'f25f9449dadd6f959e63b7b058966cea',
        'language': 'ko-KR',        
    }
    response = requests.get(base_url,params=params).json()

    if response['results'] == [] :
        return None
    else:
        if response['results'][0]['title'] == title:
            se_id = response['results'][0]['id']

        de_url = f'https://api.themoviedb.org/3/movie/{se_id}/credits'
        de_response = requests.get(de_url,params=de_params).json()
        cast_info = de_response['cast']
        crew_info = de_response['crew']
        cast_list = []
        crew_list = []
        total = {}
        for j in cast_info:
            cast_list.append(detect(j))
        for k in crew_info:
            crew_list.append(detect(k))
        cast_list = list(filter(None, cast_list))
        crew_list = list(filter(None, crew_list))
        total['cast'] = cast_list
        total['crew'] = crew_list
        return total

def detect(info):
    
    if 'cast_id' in info:
        if info['cast_id'] < 10:
            return info['name']
    elif 'department' in info:
        if info['department'] == 'Directing':
            return info['name']
    


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
