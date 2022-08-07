import requests
from pprint import pprint


def credits(title):
    pass 
    url = "https://api.themoviedb.org/3"
    path = "/search/movie"
    params = {
        "api_key" : "7b4d11acc694dae76c459794c57dd6c4",
        "language" : "ko-KR",
        'query' : f'{title}'
    }
    r = requests.get(url+path,params=params).json()
    movie_id = r.get('results')[0].get('id')
    
    path = f"/movie/{movie_id}/credits"
    params = {
        "api_key" : "7b4d11acc694dae76c459794c57dd6c4",
        "language" : "ko-KR",
    }
    get_credit = requests.get(url+path,params=params).json()
    m_cast = get_credit.get('cast')
    m_crew = get_credit.get('crew')
    dic = {'cast' : [], 'crew' : []}
    for i in range(len(m_cast)):
        if m_cast[i].get("cast_id" ) <10:
            dic['cast'].append(m_cast[i].get("name" ))
    for i in m_crew:
        if i.get('department') == 'Directing':
            dic['crew'].append(i.get('name'))
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
