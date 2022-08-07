import requests
import json
from pprint import pprint


def credits(title):
    params = {
       'api_key' : 'de3d5824ffe66b5d535f7edae4d285d6',
       'language' : 'ko',
    }
    base_url = 'https://api.themoviedb.org/3/search/movie?api_key=de3d5824ffe66b5d535f7edae4d285d6&language=ko&query='

    url = base_url+title

    res = requests.get(url,params=params).json()

    credit_id = res['results'][0]['id']
    
    

    url = f'https://api.themoviedb.org/3/movie/{credit_id}/credits'
    res = requests.get(url,params=params).json()
    output={"cast":[],"crew":[]}
    
    for r in res['cast']:
        if r['known_for_department'] =='Acting' and r['cast_id'] < 10:
            output['cast'].append(r['name'])
        
        if r['known_for_department'] == 'Directing':
            output['crew'].append(r['name'])
        
    
    return output
 


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    #{'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
      #pprint(credits('검색할 수 없는 영화'))
    # None
