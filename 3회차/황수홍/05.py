import requests
from pprint import pprint


def credits(title):
    pass 
    # 여기에 코드를 작성합니다.  
    b_url = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': '21c47128f53c4a2d7c4e8584e6fad669',
        'language': 'ko-KR',
        'query' : title
    }

    response = requests.get(b_url+path, params=params).json()
    if response['results']:
        movie_id = response['results'][0]['id']

        creditsURL = f'/movie/{movie_id}/credits'

        response = requests.get(b_url+creditsURL, params=params).json()

        cast = []
        crew = []

        for i in response['cast']:
            if i['cast_id'] < 10:
                cast.append(i['name'])
        
        for i in response['crew']:
            if i['department'] == 'Directing':
                crew.append(i['name'])
        result = {
            "cast": cast,
            "crew": crew
        }
    else:
        return None

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
