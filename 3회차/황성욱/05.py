
import requests
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)
key = os.getenv('key')

def credits(title):
    base = 'https://api.themoviedb.org/3'
    path = f'/search/movie'
    params = {
    'api_key': key,
    'language': 'ko-KR',
    'query' : title
    }
    
    response = requests.get(base+path, params=params).json()
    try:
        res = response['results']
        movie_id =  res[0]['id']
    except:
        # return "검색값이 없습니다"
        return None
    res_dict = {}
    cast_li = []
    crew_li = []
    print(res,movie_id)
    detail_path = f'/movie/{movie_id}/credits'
    response2 = requests.get(base+detail_path, params=params).json()
    raw_crew_li = response2.get('crew')
    raw_cast_li = response2.get('cast')
    for j in raw_crew_li:
        if j.get('department') == 'Directing':
            crew_li.append(j.get('name'))
    for k in raw_cast_li:
        if k.get('cast_id') < 10:
            cast_li.append(k.get('name'))
        res_dict["cast"] = cast_li
        res_dict["crew"] = crew_li
    return res_dict
    

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
