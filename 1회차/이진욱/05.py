from dotenv import load_dotenv
import os
import requests
from pprint import pprint


def credits(title):

    try:
        URL = 'https://api.themoviedb.org/3'
        path = '/search/movie'
        load_dotenv()
        pri_api_key = os.getenv('api_key')
        params = {
            'api_key': pri_api_key ,
            'language': 'ko-KR',
            'query' : title
            
        } 
        response = requests.get(URL + path, params = params).json()
        first_movie_id = response.get('results')[0].get('id')

        path2 = f'/movie/{first_movie_id}/credits'
        response2 = requests.get(URL + path2, params = params).json()

        cast_list = response2.get('cast')
        real_cast = []
        for i in range(len(cast_list)):
            if cast_list[i]['cast_id']<10:
                real_cast.append( cast_list[i]['name']  )
            
        print(real_cast)

        crew_list = response2.get('crew')
        real_crew = []
        for i in range(len(crew_list)):
            if crew_list[i]['department'] == 'Directing':
                real_crew.append( crew_list[i]['name']  )
            
        print(real_crew)
        ans_dict = {"cast":real_cast, "crew":real_crew}

        return ans_dict
    
    except IndexError:
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
