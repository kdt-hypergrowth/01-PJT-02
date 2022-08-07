import requests
from pprint import pprint


def credits(title):
    pass 
    # 여기에 코드를 작성합니다.  
    MV_URL = 'https://api.themoviedb.org/3'   #
    path1 = '/search/movie'                   

    params = {
        'api_key': '',  
        'language': 'ko-KR' ,     
        'query': title             
     }
    # title로 검색한 결과 딕셔너리안의 results 리스트를 받아옴
    rsp = requests.get(MV_URL+path1, params=params).json().get('results')

    # 검색 결과가 없다면 None 반환
    if len(rsp) == 0:
        return None

    # 검색한 영화는 검색결과의 제일 첫번째 영화
    search_movie = rsp[0]

    # 검색한 영화의 id로 cast, crew 찾기 (Get Credits)
    MV_URL = 'https://api.themoviedb.org/3'
    path2 = '/movie/'+ str(rsp[0].get('id'))+'/credits'
    params = {
        'api_key': '',
        'language': 'ko-KR',
    }

    # credit 정보 딕셔너리가 들어간 리스트
    rsp2 = requests.get(MV_URL+path2, params=params).json()

    cast_result = []
    crew_result = []

    # cast_id 값이 10 미만인 cast 추출
    cast = rsp2.get('cast')
    for i in cast:
        if i.get('cast_id') < 10:
            cast_result.append(i.get('name'))

    # department가 Directing인 crew 추출
    crew = rsp2.get('crew')
    for i in crew:
        if i.get('department') == 'Directing':
            crew_result.append(i.get('name'))

    return {"cast": cast_result, "crew": crew_result}

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
