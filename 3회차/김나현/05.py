import requests
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()
APIKEY = os.getenv('APIKEY')   # 환경변수 설정 및 가져오기

base_url = 'https://api.themoviedb.org/3'
search_path = '/search/movie'
credits_path = '/movie/{movie_id}/credits'

def credits(title):
    response = requests.get(base_url + search_path + f'?api_key={APIKEY}&language=ko-KR' + '&query='+title).json()
    # pprint(response)
    if response['total_results'] == 0:
        return None
    movies = response['results']
    # pprint(movies)
    movie_id = (movies[0])['id']
    response = requests.get(base_url + f'/movie/{movie_id}/credits' + f'?api_key={APIKEY}&language=ko-KR' + '&query='+title).json()
    cast_list = response['cast']
    crew_list = response['crew']
    res = {}
    cast = []
    crew = []
    for credit in cast_list:
        if credit['cast_id'] < 10:
            cast.append(credit['name'])
    for credit in crew_list:
        if (credit['department'] == 'Directing'):
            crew.append(credit['name'])
    res['cast'] = cast
    res['crew'] = crew
    return (res)




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
