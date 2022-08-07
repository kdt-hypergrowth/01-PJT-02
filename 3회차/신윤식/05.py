from re import S
import requests
import os
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()
s = os.environ.get('api_key')

def credits(title):
    try:
        # 영화 id값 가져오기
        Base_url = 'https://api.themoviedb.org/3'
        path_1 = '/search/movie'
        url_1 = Base_url+path_1
        params_1 = {
            'api_key':s,
            'language':'ko-KR',
            'query':title
        }
        movie_id = requests.get(url_1, params = params_1).json().get('results')[0].get('id')

        url_2 = f'https://api.themoviedb.org/3/movie/{movie_id}/credits'
        params_2 = {
            'api_key':s,
            'language':'ko-KR',
        }

        lst_case = []
        response_cast = requests.get(url_2, params = params_2).json().get('cast')
        for i in response_cast:
            if i.get('cast_id') < 10:
                lst_case.append(i.get('name'))

        lst_crew = []
        response_crew = requests.get(url_2, params = params_2).json().get('crew')
        for j in response_crew:
            if j.get('department') == 'Directing':
                lst_crew.append(j.get('name'))

        ans_dict = {
            "cast":lst_case,
            "crew":lst_crew
        }

        return ans_dict

    except:
        return None
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
'cast'
'crew'