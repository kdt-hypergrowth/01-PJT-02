from tkinter import N
import requests
from pprint import pprint


def credits(title):
    try:
        Base_URL = 'https://api.themoviedb.org/3'
        path = '/search/movie'
        params = {
            'api_key' : '036cba43a53da3f3d64b768b2cc83862',
            'language' : 'ko-KR',
            'query' : title
        }
        response = requests.get(Base_URL + path, params=params).json()
        m_id = response.get('results')[0].get('id')
        
        path2 = f'/movie/{m_id}/credits'
        params_2 = {
            'api_key' : '036cba43a53da3f3d64b768b2cc83862',
            'language' : 'ko-KR'
        }
        response2 = requests.get(Base_URL + path2, params=params_2).json()
        # key = id cast crew
        movie_credits = {"cast" : [], "crew" : []}
        
        for idx in range(len(response2.get('cast'))):
            if response2.get('cast')[idx].get('cast_id') < 10:
                movie_credits['cast'].append(response2.get('cast')[idx].get('name'))
                
        for idx in range(len(response2.get('crew'))):
            if response2.get('crew')[idx].get('department') == 'Directing':
                movie_credits['crew'].append(response2.get('crew')[idx].get('name'))
        
        return movie_credits
    # 검색결과 일치하는 영화가 없을때 IndexError: list index out of range 에러 발생
    # IndexError에러를 예외처리 
    except IndexError:
        return None
    # 여기에 코드를 작성합니다.  


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
