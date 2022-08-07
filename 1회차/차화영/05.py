import requests
from pprint import pprint
from dotenv import load_dotenv
import os

def credits(title):
    load_dotenv()
    key = os.getenv('80c8b18bf43a69499e913dc21300b23c') 
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {'api_key': '80c8b18bf43a69499e913dc21300b23c',
    'language': 'ko-KR',
    'query': title
    }

    response = requests.get(BASE_URL+path, params=params)
    if response.json()['results']:
        movie_id = response.json()['results'][0]['id']
        # 첫번째 영화[0]의 id값을 활용
        path = f'/movie/{movie_id}/credits'
        # f string으로 movie_id 입력 후 credits 목록 반환
        response = requests.get(BASE_URL+path, params=params).json()

        actor = response.get('cast')
        # .get() : response라는 딕셔녀리에서 'cast' key에 대응되는 value값을 돌려준다.
        staff = response.get('crew')
        # .get() : response라는 딕셔너리에서 'crew' key에 대응되는 value값을 돌려준다.
        cast = []
        # cast라는 키를 생성 - 리스트로 출력된다.
        crew = []
        # crew라는 키를 생성 - 리스트로 출력된다.
        
        for i in range(len(actor)):
            # len 함수는 리스트 안의 요소 개수를 돌려주는 함수이다. 따라서 range(len(actor))의 범위만큼 i가 반복된다.
            if actor[i].get('cast_id') < 10:
                # .get() : actor 딕셔너리에서 'name' key에 대응되는 value값을 돌려준다.
                cast.append(actor[i].get('name'))
                # cast에 'name' 리스트 추가
        for i in range(len(staff)):
            # len 함수는 리스트 안의 요소 개수를 돌려주는 함수이다. 따라서 range(len(staff))의 범위만큼 i가 반복된다.
            if staff[i].get('department') == 'Directing':
                # .get() : staff 딕셔너리에서 'name' key에 대응되는 value값을 돌려준다.
                crew.append(staff[i].get('name'))
                # crew에 'name' 리스트 추가
        credits_list = {'cast' : cast, 'crew' : crew}
        # key가 'cast'와 'crew'로 구성된 credits_list, value는 append로 리스트가 추가된 cast와 crew
    else:
        credits_list = None    
    
    return credits_list

# 아래의 코드는 수정하지 않습니다..
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
