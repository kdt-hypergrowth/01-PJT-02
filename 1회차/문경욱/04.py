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


def recommendation(title):
    movie_id = search(title) # search 함수르 통해 얻어온 아이디를 movie_id에 저장

    if movie_id == None: # movie_id에 NONE이 저장되어 있다면,
        return None # None을 반환
    url = 'https://api.themoviedb.org/3'
    path = f'/movie/{movie_id}/recommendations'

    params = {
        'api_key' : api_key,
        'language': 'ko-KR'
    }

    response = requests.get(url + path, params=params).json().get('results')

    movie_list = []

    for i in range(len(response)):
        movie_list.append(response[i].get('title')) # movie 리스트에 영화 제목들을 추가
    
    if movie_list == []: # 만약 리스트가 비었다면
        return [] # 빈 리스트 반환
    else: # 리스트가 비어있지 않으면
        return movie_list # 그대로 movie_list를 출력


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
