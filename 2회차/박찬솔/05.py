import requests
from pprint import pprint

# 출연진 및 연출진 데이터 조회
# 영화의 출연진(cast) 그리고 스태프(crew) 중 연출진으로 구성된 목록만을 출력
# requests 라이브러리를 활용하여 TMDB에서 영화제목으로 영화를 검색(Search Movies)
# 첫번째 영화의 id 값을 활용하여 TMDB에서 해당 영화에 대한 출연진과 스태프 목록(Get Credits)을 가져옵니다.
# 출연진 중 cast_id 값이 10 미만인 출연진만 추출하고, 연출진은 부서(department)가 Directing 인 데이터만 추출
# cast 와 directing 으로 구성된 딕셔너리에 추출된 값을 리스트로 출력하는 함수를 작성
def credits(title):
    pass 
    # 여기에 코드를 작성합니다.  
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
    'api_key': '474c622ef9ff33b07a0bac17dd3e0ff2',
    'language': 'ko-KR',
    'query' : title
    }
    response = requests.get(BASE_URL+path,params=params).json().get('results', None)
    if response == []:
        return None

    result_dict = {'cast':[], 'crew':[]}
    response_id = response[0].get('id')
    movie_id = response_id

    BASE_URL2 = 'https://api.themoviedb.org/3'
    path2 =f'/movie/{movie_id}/credits'
    params2 ={
    'api_key' : '474c622ef9ff33b07a0bac17dd3e0ff2',
    'language' : 'ko-KR',
    'query':title
    }
    response2 = requests.get(BASE_URL2+path2, params = params2).json()
  
    cast_list = response2.get('cast')
    crew_list = response2.get('crew')
  
    for actor in response2['cast']:
        if actor['cast_id'] < 10:
            result_dict['cast'].append(actor['name'])

    for crew in response2['crew']:
        if crew['department'] == 'Directing':
            result_dict['crew'].append(crew['name'])
    return result_dict      
    
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
