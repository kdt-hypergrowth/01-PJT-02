import requests as r
from pprint import pprint
from dotenv import load_dotenv
import os 

load_dotenv()

def credits(title):
    pass 
    # 여기에 코드를 작성합니다.  
    base_url = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': os.environ.get('api_key'),
        'language': 'ko-KR',
        'query': {title}
    }
    response = r.get(base_url+path, params=params).json()

    try:
        response = (response['results'])[0]
        movie_id = response['id']
        
        result_dict = {}
        
        cast_path = f'/movie/{movie_id}/credits'
        cast_params = {
            'api_key': os.environ.get('api_key'),
            'language': 'ko-KR',
        }
        
        cast_response = r.get(base_url+cast_path, params=cast_params).json()
        
        cast_list = []
        crew_list = []
        
        cast = cast_response['cast']
        crew = cast_response['crew']
        
        for person in cast:
            if person.get('cast_id') < 10:
                cast_list.append(person['original_name'])
                
        for person in crew:
            if person.get('department') == 'Directing':
                crew_list.append(person['name'])
                
        result_dict.update({'cast': cast_list, 'crew': crew_list})
        return result_dict

    except:
        return None

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
