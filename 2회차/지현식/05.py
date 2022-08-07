import requests
from pprint import pprint
def search(title):
    url = 'https://api.themoviedb.org/3'
    path = '/search/movie'

    params = {
        'api_key': '3d086799f6ddf19a461e5ed8f4712adf',
        'language': 'ko-KR',
        'query': f'{title}'
    }
    response = requests.get(url + path, params=params).json().get('results')
    for i in range(len(response)):
        return response[i].get("id")

def credits(title):
    movie_id = search(title)
    if movie_id == None:
        return None
    url = 'https://api.themoviedb.org/3'
    path = f'/movie/{movie_id}/credits'

    params = {
        'api_key': '3d086799f6ddf19a461e5ed8f4712adf',
        'language': 'ko-KR'
    }

    response = requests.get(url + path,params=params).json()

    crews = response.get('crew')
    casts = response.get('cast')

    crew = []
    cast = []
    for i in range(len(crews)):
        if crews[i].get('department') =='Directing':
            crew.append(crews[i].get('name'))
    for i in range(len(casts)):
        if casts[i].get('cast_id') < 10:
            cast.append(casts[i].get('name'))
    answer = {"cast":cast, "crew":crew}
    return answer
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
