import requests
from pprint import pprint


def credits(title):
    pass

    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    # 영화 제목으로 영화를 검색

    params = {
        'api_key' : '143e53e7e83b57a0c8376b3020cd5051',
        'language': 'ko',
        'query' : title
    }
# url를 통해 서버에 요청해서 응답받고, json타입 데이터를 dictionary타입으로 바꿔 변수에 저장
    response = requests.get(BASE_URL+path, params=params).json()
    
    if response['results']:
        movies_id = response['results'][0]['id']
        # 변수를 지정해주고, 영화검색에서 받은 결과중 첫번째 영화 id 값을 이용하여 영화 목록을 가져오기
    else:
        return None

    BASE_URL ='https://api.themoviedb.org/3'   
    path2 = f'/movie/{movies_id}/credits'
    params2 = {
        'api_key' : '143e53e7e83b57a0c8376b3020cd5051',
        'language': 'ko',
        'query' : movies_id
    }
    # movie_id 값을 이용해 추천 목록을 받을것
    response2 = requests.get(BASE_URL+path2, params2).json()
    

    cast = []    
    for i in response2["cast"]:
        if i['cast_id'] < 10:
            cast.append(i['name'])
            # 10 미만인 인물들의 이름을 cast 폴더에 저장


    crew = []
    for j in response2["crew"]:
        if j['department'] == 'Directing':
            crew.append(j['name'])
            # departmet 값이 "Directing"인 인물들의 이름을 crew 폴더에 저장
    
    person = {}
    person["cast"] = cast
    person["crew"] = crew
    # 두 개를 키 값으로 각 리스트 들을 설정하여 딕셔너리에 넣는다.

    return person


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
