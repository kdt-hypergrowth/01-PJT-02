import requests
from pprint import pprint


def credits(title):
    url = 'https://api.themoviedb.org/3'
    path1 = '/search/movie'
    params = {
        'api_key': '26eaac93f79c23ac640e6c7c91fb93af',
        'language': 'ko-KR',
        'query' : title
    }

    movie_data = requests.get(url+path1, params=params).json()
    
    if movie_data.get('results'):
        movieid = movie_data.get('results')[0].get('id')
    else:
        movieid = None
    
    
    movie_id = movieid
    path2 = f'/movie/{movie_id}/credits'
    movie_recommend = requests.get(url+path2, params=params).json()
    
    try:
        ca = []
        for people in movie_recommend.get('cast'):
            if people.get('cast_id') < 10:
                ca.append(people.get('name'))
        cr = []
        for depart in movie_recommend.get('crew'):
            if depart.get('department') == 'Directing':
                cr.append(depart.get('name'))
    except:
        return 

    result = {} 
    result['cast'] = ca
    result['crew'] = cr
    
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


