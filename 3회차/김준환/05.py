import requests
from pprint import pprint


def credits(title):
    pass 
    # 여기에 코드를 작성합니다.  
    base_url = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': 'e2be94a1762b4b81af8b205d5e2bcb5f',
        'language': 'ko-KR',
        'query': title
    }
    response = requests.get(base_url+path, params=params).json()
    if len(response['results']) < 1:
        return None
    mv_id = response['results'][0]['id']

    base_url_2 = 'https://api.themoviedb.org/3'
    path_2 = f'/movie/{mv_id}/credits'
    params_2 = {
        'api_key': 'e2be94a1762b4b81af8b205d5e2bcb5f',
        'language': 'ko-KR'
    }
    response_2 = requests.get(base_url_2+path_2, params=params_2).json()
    dic = {}
    dic['cast'] = []
    dic['crew'] = []
    for i in range(len(response_2['cast'])):
        if response_2['cast'][i]['cast_id'] < 10:
            dic['cast'].append(response_2['cast'][i]['name'])
    for i in range(len(response_2['crew'])):
        if response_2['crew'][i]['department'] == 'Directing':
            dic['crew'].append(response_2['crew'][i]['name'])

    return dic
    

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
