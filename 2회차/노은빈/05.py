import requests
from pprint import pprint

def credits(title):
    base_url = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': '8b431f95b8d1aca3b694e017ecd9c4fb',
        'language': 'ko-KR',
        'query': title
    }

    response = requests.get(base_url + path, params=params).json()  
    movies = response.get('results')

    if response == None:
        return None

    else:
        movie_id = movies[0]['id']  
    #영화 검색 결과 중 첫번째 영화를 id 값을 이용해 추천 목록으로 가져와 그 값을 변수로 지정

    base_url = 'https://api.themoviedb.org/3'
    path = f'/movie/{movie_id}/credits'
    params = {
        'api_key': '8b431f95b8d1aca3b694e017ecd9c4fb',
        'language': 'ko-KR'
    }

    response = requests.get(base_url + path, params=params).json()  
    casts = response.get('cast')
    crews = response.get('crew')
    castss = []
    crewss = []  #cast와 crew 모두 리스트로 출력

    for i in casts:
        cast_id = i.get('cast_id')
        if cast_id < 10:   #cast_id 값이 10 미만
            castss.append(i.get('name'))

    for j in crews:
        department = j.get('department')
        if department == 'Directing':  #연출진은 department가 Directing인 사람만
            crewss.append(j.get('name'))

    result = {"cast" : castss, "crew" : crewss}  #result는 딕셔너리

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
