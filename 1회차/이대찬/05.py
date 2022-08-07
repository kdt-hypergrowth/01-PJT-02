import requests
from pprint import pprint


def credits(title):
    URL = 'https://api.themoviedb.org/3/search/movie'
    
    params = {
        'api_key' : '0de00acda6081b7131fa382c50d91123',
        'language' : 'ko-KR',
        'query' : title
    }
    response = requests.get(URL, params=params).json()
    a= response.get('results')
    if len(a) == 0:
        return None
    b= a[0]['id']
    
     
    URL2 =f'https://api.themoviedb.org/3/movie/{b}/credits'
    params2 = {
        'api_key' : '0de00acda6081b7131fa382c50d91123',
        'language' : 'ko-KR',

    }
    c = requests.get(URL2, params = params2).json()
    d= c.get('cast')
    t1 = []
    for i in d:
        if i['cast_id'] < 10:
            t1.append(i['name'])
    
    e= c.get('crew')
    t2 =[]
    for i in e:
        if i['department'] == 'Directing':
            t2.append(i['name'])
     
    result = {"cast" : t1, "crew" : t2}
    return result

    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    #pprint(credits('검색할 수 없는 영화'))
    # None
