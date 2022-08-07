import requests
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('api_key')


def search(title): # search라는 함수를 정의
    url = 'https://api.themoviedb.org/3' 
    path = '/search/movie'

    params = {
        'api_key' : api_key,
        'language': 'ko-KR',
        'query': f'{title}' # 검색할 영화 제목을 query로 받음
    }
    response = requests.get(url + path, params=params).json().get('results')  

    for i in range(len(response)): #respons 횟수만큼 진행
        return response[i].get("id") # response 리스트 안에 있는 딕셔너리에서 'id'의 value값을 불러옴


def credits(title):
    movie_id = search(title)
    if movie_id == None:
        return None
    url = 'https://api.themoviedb.org/3'
    path = f'/movie/{movie_id}/credits'

    params = {
        'api_key' : api_key,
        'language': 'ko-KR'
    }

    response = requests.get(url + path,params=params).json()

    crew = response.get('crew')
    cast = response.get('cast')

    crew_list = []
    cast_list = []

    for i in range(len(crew)): # JSON 파일에서 crew의 총 인원만큼 반복
        if crew[i].get('department') =='Directing': # 만약 부서가 Directing이면
            crew_list.append(crew[i].get('name')) # crew_list에 name 추가

    for i in range(len(cast)): #json 파일에서 cast의 총 인원만큼 반복
        if cast[i].get('cast_id') < 10: # 만약 cast_id가 10보다 작으면
            cast_list.append(cast[i].get('name')) # cast_list에  name 추가

    credits = {"cast": cast_list, "crew": crew_list}

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
