import requests
from pprint import pprint


def credits(title):
    pass 
    # 여기에 코드를 작성합니다.  
    url = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': '42259abc0f3225655eba5deb9d51f7f3',
        'language': 'ko-KR',
        'query': title
    }
    re = requests.get(url+path, params=params).json()
    id=re.get('results')
    if not id:
        return 
    id2 = id[0]['id']
    
    path2 = f'/movie/{id2}/credits'
    params2 = {
        'api_key': '42259abc0f3225655eba5deb9d51f7f3',
        'language': 'ko-KR'
    }
    re2 = requests.get(url+path2, params=params2).json()    
    c1 = re2.get('cast')
    c2 = re2.get('crew')
    credit_result = {'cast':[], 'crew':[]}
    for i in c1:
        cid = i.get('cast_id')
        if cid < 10:
            credit_result['cast'].append(i.get('name'))

    for j in c2:
        if j['department'] == 'Directing':
            credit_result['crew'].append(j.get('name'))
    return credit_result

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
    