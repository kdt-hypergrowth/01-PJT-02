import requests
from pprint import pprint


def credits(title):

    # 영화 제목을 통해 영화 ID 가져오기
    base_url = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key' : '652241f716c0f8b8f5006465a644f600',
        'language': 'ko-KR',
        'query' : title
    }

    response = requests.get(base_url + path, params = params).json().get('results')

    if len(response) == 0:
        return None
    else:
        id = response[0]['id']

    # 여기서부터는 영화 credits 관련
    path = f'/movie/{id}/credits'
    
    response = requests.get(base_url + path, params = params).json()
    
    # response_cast (타입: 리스트)를 'i' 딕셔너리로 만든 후,
    # 딕셔너리 안에 있는 key 중 'cast_id'의 value를 찾고
    # 그 value가 10미만이면
    # 'cast', 리스트 변수 안에 배우 이름 'name' 들을 넣은다.
    cast = []
    response_cast = response.get('cast')

    for i in response_cast:
        if i['cast_id'] < 10:
            cast.append(i['name'])
    
    # response_crew (타입: 리스트)를 'i' 딕셔너리로 만든 후,
    # 딕셔너리 안에 있는 key 중 'department'의 value를 찾고
    # 문자열이 ('Directing') 동일하면 
    # 'crew', 리스트 변수 안에 연출진 이름 'name' 들을 넣은다.
    crew = []
    response_crew = response.get('crew')
    for i in response_crew:
        if i['department'] == 'Directing':
            crew.append(i['name'])

    return {
        'cast': cast,
        'crew': crew
    }


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    # pprint(credits('검색할 수 없는 영화'))
    # None
