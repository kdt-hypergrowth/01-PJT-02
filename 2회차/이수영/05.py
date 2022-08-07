import requests
from pprint import pprint

def credits(title):
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key':'dcc1e7ed069f7427a2816e92b32e7c8b',
        'language': 'ko-KR',
        'query': title
        }
    response = requests.get(BASE_URL+path, params = params).json()
    movies = response.get('results')
    if movies ==[]:
        result = 'none'
    else:
        first_id = movies[0]['id']
        path_2 = f'/movie/{first_id}/credits'
        params = {
            'api_key':'dcc1e7ed069f7427a2816e92b32e7c8b',
            'language': 'ko-KR'
            }
        response = requests.get(BASE_URL+path_2, params = params).json()
        casts = response.get('cast')
        crews = response.get('crew')
        main = []
        for cast in casts:
            if cast['cast_id'] < 10:
                main.append(cast)
        Fame = []
        for act in main:
            Fame.append(act['name'])
        people = []
        for crew in crews:
            if crew['department'] == 'Directing':
                people.append(crew)
        emp = []
        for person in people:
            emp.append(person['name'])
        all = {'cast': Fame, 'crew': emp}
        return all

        
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
