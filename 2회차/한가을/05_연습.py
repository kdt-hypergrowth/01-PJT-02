from pprint import pprint
import requests

def credits(title):
    pass


    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': 'd84fbf5eb517d499e6c3ce37311d4394',
        'language': 'ko-KR',
        'query': title
    }

    response = requests.get(BASE_URL + path, params=params).json()
    result = []

    if response['results']:
        movie_id = response['results'][0]['id']
        path = f'/movie/{movie_id}/recommendations'

        params = {
            'api_key': 'd84fbf5eb517d499e6c3ce37311d4394',
            'language': 'ko-KR',
            'movie_id': movie_id
        }

        people_dict = requests.get(BASE_URL + path, params=params).json()


        if 'success' in people_dict.keys():
            return None
        
        result_dict = {'cast' : [], 'crew' : []}

        for actor in people_dict['cast']:
            if actor['cast_id'] < 10:
                result_dict['cast'].append(actor['name'])

        for crew in people_dict['crew']:
            if crew['department'] == 'Directing':
                result_dict['crew'].append(crew['name'])
        return result_dict

if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None