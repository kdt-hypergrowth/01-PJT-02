import requests
from pprint import pprint


def credits(title):
    pass 
    # 여기에 코드를 작성합니다.  
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': '66c53dabd7bc9afc53c2ca7eba855583',
        'language' : 'ko-KR',
        'query' : title
    }
    response = requests.get(BASE_URL+path, params=params).json()
    try :
        for tt in response['results']:
            if title == tt['title']:
                movie_id = tt['id']
        
        credit_path = f'/movie/{movie_id}/credits'
        credit_response = requests.get(BASE_URL+credit_path, params=params).json()
        _list = {'cast':[],'crew':[]}
        for cast in credit_response['cast']:
            name = cast['name']
            if name not in _list['cast']:
                _list['cast'].append(name)
        for crew in credit_response['crew']:
            name = crew['name']
            if name not in _list['crew']:
                _list['crew'].append(name)
        return _list
    except :
        return None
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 
    주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
