import requests
from pprint import pprint


def credits(title):
    # API를 받아올 주소
    BASIC_URL = 'https://api.themoviedb.org/3'
    # search 주소
    path = '/search/movie'
    # 내 api 키와 언어 설정
    params = {
      'api_key': 'ec5782cbc602381ddeeedd23dcf585b9',
      'language': 'ko',
      'region': 'KR',
      'query': title
    }
     # 영화 홈페이지 받아오기
    response = requests.get(BASIC_URL + path, params=params).json()
    
    # 홈페이지에서 리절트 정보를 받아온다
    if response.get('results'):
        # results에 첫번째로 id를 가져온다? 
        id1 = response.get('results')[0].get('id')
    # 그렇지 않다면 id1은 None
    else :
        id1 = None

    # movie id가 id1에 있다
    movie_id = id1

    # 추천 홈페이지 받아오기;
    path2= f'/movie/{movie_id}/credits'
    # 내 api 키와 언어 설정
    params_2 = {
            'api_key':'ec5782cbc602381ddeeedd23dcf585b9',
            'language':'ko-KR',
        }

    # cast 홈페이지 받아오기;
    res = requests.get(BASIC_URL + path2, params=params_2).json().get('cast')

    # 받아올 리스트 추가
    cast_list = []
    
    #  cast 홈페이지안에 i가 있다면
    for i in res:
        #cast_id를 받아오면 
       if i.get('cast_id'):
        # cast_list에 cast_id에있는 이름을 리스트에 추가해라
            cast_list.append(i.get('name'))

   
    # 받아올 리스트 추가
    directing_list = []
    # crew 홈페이지 받아오기;
    res1 = requests.get(BASIC_URL + path2, params=params_2).json().get('crew')
    
     # crew 홈페이지안에 i가 있다면
    for j in res1:
        # 만약 j에서 받아오는 department가 Directing과 같다면
        if j.get('department') =='Directing':
            #j에 값에 이름을 directing_list에 추가해라
            directing_list.append(j.get('name'))
    
    
    ans_dict = {
            "cast": cast_list,
            "crew":directing_list
        }
    return ans_dict

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
