import requests
from pprint import pprint


def credits(title):
    params = {
        'api_key' : '',
        'language' : 'ko-KR',
        'query' : f'{title}'
    }
    base_url = 'https://api.themoviedb.org/3'
    search_url = "/search/movie"
    response = requests.get(base_url + search_url, params=params).json()
    if response.get('results') == []:
        return None
    else:
        # 검색 결과의 첫 번째 영화의 id
        movie_id = response.get('results')[0].get('id')
        
        # 출연진 및 연출진 찾기
        credits_url = f"/movie/{movie_id}/credits"
        params_2 = params = {
            'api_key' : 'a926205337e50c1326d01b6b82f037cd',
            'language' : 'ko-KR',
        }
        get_credits_response = requests.get(base_url + credits_url, params=params_2).json()
        
        # 조건에 맞는출연진과 연출진의 정보를 빈 딕셔너리에 저장
        credits = {"cast" : [], "crew" : []}
        # 출연진 cast_id < 10
        for cast in get_credits_response.get('cast'):
            if cast.get('cast_id') < 10:
                credits['cast'].append(cast.get('name'))
        # 연출진 department == Directing
        for crew in get_credits_response.get('crew'):
            if crew.get('department') == 'Directing':
                credits['crew'].append(crew.get('name'))
                
    return credits


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
