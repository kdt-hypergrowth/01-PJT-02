import requests
from pprint import pprint


def credits(title):
    pass 
    # 여기에 코드를 작성합니다.  
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': 'e3ebcaf0cb86336e3fa61579f1f0569b',
        'language': 'ko-KR',
        'query': title 
        # 제목을 입력하여 결과를 받을 것이기 때문에 'query : title'을 추가
    }
    res = requests.get(BASE_URL + path, params=params).json()

    if res['results']:
        movie_id = res['results'][0]['id']

        path2 = f'/movie/{movie_id}/credits'
        params2 = {
        'api_key': 'e3ebcaf0cb86336e3fa61579f1f0569b',
        'language': 'ko-KR',
        'query' : movie_id
        }
        res2 = requests.get(BASE_URL + path2, params=params2).json()
        cast = []
        for i in res2['cast']:
            if i['cast_id'] < 10:
                cast.append(i['name'])
        crew = []
        for  j in res2['crew']:
            if j['department'] == 'Directing':
                crew.append(j['name'])
        person = {}
        person['cast'] = cast
        person['crew'] = crew
        return person

    else:
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
