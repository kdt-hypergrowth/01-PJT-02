
#* 제공된 영화 제목을 검색하여 해당 영화의 출연진(`cast`) 그리고 스태프(`crew`) 중 연출진으로 구성된 목록만을 출력합니다.
#* requests 라이브러리를 활용하여 TMDB에서 영화제목으로 영화를 검색(Search Movies)합니다.
#* 응답 받은 결과 중 첫번째 영화의 id 값을 활용하여 TMDB에서 해당 영화에 대한 출연진과 스태프 목록(Get Credits)을 가져옵니다.
#* 출연진 중 `cast_id` 값이 `10 미만`인 출연진만 추출하고, 연출진은 부서(`department`)가 `Directing` 인 데이터만 추출합니다.
#* `cast` 와 `directing` 으로 구성된 딕셔너리에 추출된 값을 리스트로 출력하는 함수를 작성합니다.
import requests
from pprint import pprint

def credits(title):
    title = input()
    # 예시로 기생충 입력하자
    BASE_URL = 'https://api.themoviedb.org/3'
    search_path = f'/search/movie?api_key=617e47b888d4519a585f9f4cd8bbab6e&language=ko-KOR&page=1&include_adult=false&query={title}'
    search_URL = BASE_URL + search_path

    search_result = requests.get(search_URL).json()
    movie_id = search_result['results'][0]['id']
    # 마찬가지로 search_result를 이용해서 첫번째 영화의 id 값에 접근했고
    # 이번엔 첫번째 영화 id를 이용해서 출연진과 스태프가 있는 json파일을 요청!

    credits_path = f'/movie/{movie_id}/credits?api_key=617e47b888d4519a585f9f4cd8bbab6e&language=ko-KOR'
    credits_URL = BASE_URL + credits_path
    credits_movie = requests.get(credits_URL).json()
    actor_list = []
    director_list = []
    
    # 배우와 감독진을 나눠야 하므로 리스트 2개 각각 생성 하고 조건 따라서 append하기
    #* 1. 배우들 리스트에 추가
    for movie in credits_movie['cast']:
        if movie['cast_id'] < 10:
            actor_list.append(movie['name'])
    #* 2. 스태프들 리스트에 추가   
    for movie in credits_movie['crew']:
        if movie['department'] == 'Directing':
            director_list.append(movie['name'])
    # cast와 crew가 key이고 각각 해당하는 리스트를 value로 가지는 딕셔너리 형태로 return 해야함
    result_dict = {
        "cast" : actor_list,
        "crew" : director_list,
    }
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
