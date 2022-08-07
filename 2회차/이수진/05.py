import requests
from pprint import pprint


def credits(title):
    url = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key':'db73cdf92f64511f998356227c82b682',
        'language':'ko-KR',
        'query': title
    }
    response = requests.get(url+path,params=params).json().get('results')
    if len(response) == 0 :
        return None
    else :
        movie_id = response[0]['id']
    
    url = 'https://api.themoviedb.org/3'
    path = f'/movie/{movie_id}/credits'
    params = {
        'api_key':'db73cdf92f64511f998356227c82b682',
        'language':'ko-KR'
    }
    response = requests.get(url+path,params=params).json()
    result = {'cast':[],'crew':[]}
    for i in response['cast']:
        if i['cast_id'] < 10 :
            result['cast'].append(i['name'])
    for i in response['crew']:
        if i['department'] == 'Directing':
            result['crew'].append(i['name'])
    return result

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
