import requests
from pprint import pprint


def credits(title):
    URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
         'api_key': 'd1c47d9288b0354c3305720bd5e426e7',
         'language': 'ko-KR',
         'query': title
     }
    response = requests.get(URL+path, params=params).json().get('results')
    
    # 영화 id 검색에 실패할 경우 None을 반환 
    if len(response) == 0:
         return None
    
    # 응답 받은 결과 중 첫번째 영화의 id 값을 활용
    search_movie = response[0]

    URL = 'https://api.themoviedb.org/3'
    path = '/movie/'+ str(response[0].get('id')) + '/credits'
    params = {
         'api_key': 'd1c47d9288b0354c3305720bd5e426e7',
         'language': 'ko-KR',
        }
    response = requests.get(URL+path, params=params).json()
    
    cast_list = []
    crew_list = []

    # cast_id 값이 10 미만인 cast 
    cast = response.get('cast')
    for i in cast:
        if i.get('cast_id') < 10:
            cast_list.append(i.get('name'))

    # department가 Directing인 crew 
    crew = response.get('crew')
    for i in crew:
        if i.get('department') == 'Directing':
            crew_list.append(i.get('name'))

    # cast 와 directing 으로 구성된 딕셔너리에 추출된 값을 리스트로 출력
    return {"cast": cast_list, "crew": crew_list}

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
