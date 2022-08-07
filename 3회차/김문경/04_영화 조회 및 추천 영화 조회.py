
#* 영화 제목으로 검색을 하여 추천 영화 목록을 출력합니다.
#* requests 라이브러리를 활용하여 TMDB에서 영화제목으로 영화를 검색(Search Movies)합니다.
#* 응답 받은 결과 중 첫번째 영화의 id 값을 활용하여 TMDB에서 추천 영화 목록(Get Recommendations)을 가져옵니다.
#* 추천 영화 목록을 리스트로 반환하는 함수를 작성합니다.
from numpy import rec
import requests
from pprint import pprint

# search movie 로 영화를 하나 검색하고 그 영화의 id를 이용해서 get recommentdations를 이용
#* 즉 2번 사용해야함!

def recommendation(title):
    title = input()
    BASE_URL = 'https://api.themoviedb.org/3'
    search_path = f'/search/movie?api_key=617e47b888d4519a585f9f4cd8bbab6e&language=ko-KOR&page=1&include_adult=false&query={title}'
    search_URL = BASE_URL + search_path

    search_result = requests.get(search_URL).json()
    movie_id = search_result['results'][0]['id']
    # search_result를 이용해서 첫번째 영화의 id 값에 접근했고
    # 이 값을 이용해서 recommendation을 한 번 더 사용!
    
    recommend_path = f'/movie/{movie_id}/recommendations?api_key=617e47b888d4519a585f9f4cd8bbab6e&language=ko-KOR&page=1'
    recommend_URL = BASE_URL + recommend_path
    recommend_movies = requests.get(recommend_URL).json()['results']
    recommend_list = []
    for movie in recommend_movies:
        recommend_list.append(movie['title'])
    return recommend_list

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
