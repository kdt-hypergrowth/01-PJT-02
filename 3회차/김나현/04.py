import requests
from pprint import pprint
from dotenv import load_dotenv
import os


load_dotenv()
APIKEY = os.getenv('APIKEY')   # 환경변수 설정 및 가져오기

base_url = 'https://api.themoviedb.org/3'
recommend_path = '/movie/{movie_id}/recommendations'
search_path = '/search/movie'

def recommendation(title):

    response = requests.get(base_url + search_path + f'?api_key={APIKEY}&language=ko-KR' + '&query=' + title).json()
    # pprint(response)
    if response['total_results'] == 0:
        return None
    movie = response['results']
    # pprint(movie)
    movie_id = (movie[0])['id']
    # print(movie_id)
    response = requests.get(base_url + f'/movie/{movie_id}/recommendations' + f'?api_key={APIKEY}&language=ko-KR').json()
    # pprint(response)
    res = []
    movie_list = response['results']
    for movie in movie_list:
        res.append(movie['title'])
    return res




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
