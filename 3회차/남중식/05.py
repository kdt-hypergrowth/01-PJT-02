import requests
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY_TOKEN = os.getenv('my_api_key')


def credits(title):
    pass 
    # 여기에 코드를 작성합니다.  
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': API_KEY_TOKEN,
        'language': 'ko-KR',
        'query': title
    }
    
    response = requests.get(BASE_URL+path, params=params).json() 
    result = response.get('results')
    
    # 영화 이름 검색 결과 없을 시, None 반환
    if result == []:
        return None
    
    # 영화 이름 검색 첫번째 결과의 id 값
    res_id = result[0].get('id')
    movie_id = res_id
    
        # 여기에 코드를 작성합니다.  
    BASE_URL2 = 'https://api.themoviedb.org/3'
    path2 = f'/movie/{movie_id}/credits'
    params2 = {
        'api_key': 'f813cc9773fb55369f6d3e1dae17ba81',
        'language': 'ko-KR',
        'query': title
    }
    
    response_for_credits = requests.get(BASE_URL2+path2, params=params2).json()
    
    cast_list_response = response_for_credits.get('cast')
    crew_list_response = response_for_credits.get('crew')
    
    cast_list = []
    crew_list = []
    
    for c in cast_list_response:
        if c.get('cast_id') < 10:
            cast_list.append(c.get('name'))
            
    for c in crew_list_response:
        if c.get('department') == 'Directing':
            crew_list.append(c.get('name'))
    
    return_dict = {}
    return_dict['cast'] = cast_list
    return_dict['crew'] = crew_list
    
    return return_dict
    
    



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
