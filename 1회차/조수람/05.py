import os
import requests
from pprint import pprint
from dotenv import load_dotenv

def credits(title):

##########################################################################################
# 1. 기본 영화 설정
##########################################################################################
    print(f"'{title}' 참여한 배우 & 스탭")

    load_dotenv()
    api_key = os.getenv('api_key')
    query = f"query={title}"

##########################################################################################
# 2. title로 받은 영화의 id 확인
##########################################################################################

    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&{query}" #키워드(Query)를 통해, 특정 영화 정보 서치

    response = requests.get(url).json() 
    # pprint(response)

    movie_list = response['results']
    movie_id = movie_list[0]['id']
    # print(movie_id, type(movie_id))


##########################################################################################
# 3. 영화 id기반으로 cast & crew 목록 받아오기
##########################################################################################

    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}"

    response = requests.get(url).json()

    # print(type(response), response.keys()) ## 이거 저장해두기 

    # pprint(response['crew'][0])

    cast_list = []
    directing_crew_list = []
    
    for dict in response['cast']:
        if dict['cast_id'] < 10:
            cast_list.append(dict['name'])
    
    for dict in response['crew']:
        if dict['department'] == 'Directing':
            directing_crew_list.append(dict['name'])

    cast_n_crew = {"cast": cast_list, "crew": directing_crew_list}

    return cast_n_crew


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
