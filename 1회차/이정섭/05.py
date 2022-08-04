import requests
from pprint import pprint

def credits(title):

    movie_id = search(title)
    if movie_id == None:
        return None

    Base_URL = 'https://api.themoviedb.org/3'
    path = f'/movie/{movie_id}/credits'
    params = {
    'api_key': '223131069bc4ff601e73529b7eb1b275'
              }
    response = requests.get(Base_URL+path, params=params).json()

    if response == None:
        return None
   
    else:
        casts = response.get('cast')
        crews = response.get('crew')
        movie_dict = {"cast":[], "crew":[]}
        
        for cast in casts:
            if cast.get('cast_id') < 10: 
                movie_dict['cast'].append((cast.get('name'))) 
        
        for crew in crews:
            if crew.get('department') == "Directing": 
                movie_dict['crew'].append((crew.get('name'))) 

        return movie_dict 

def search(title):
    movie_id = None
    Base_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
    'api_key': '223131069bc4ff601e73529b7eb1b275',
    'query': f'{title}'
              }
    response = requests.get(Base_URL+path, params=params).json()

    if response == None:
        return None
    
    else:
        results = response.get('results') 
        for x in range(len(results)):
            movie_id = results[0].get('id') 
       
        return movie_id

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
