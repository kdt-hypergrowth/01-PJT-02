import requests
from pprint import pprint
import requests
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv('api_key')


def credits(title):
    URL ='https://api.themoviedb.org/3/'
    
        
    path1 = 'search/movie'
    params1 ={
            'api_key':api_key ,
            'query' : title,
            'language':'ko-KR'
        }
    respond1 = requests.get(URL + path1 , params = params1).json()
    credit_search = respond1.get('results')
    if credit_search != [] :
        movie_id = credit_search[0].get('id')
    else :
        movie_id = 0    


    path2 = f'movie/{movie_id}/credits'
    params2 ={
            'api_key':'c85b6b9693031d62b3c34274ee1a726a' ,
            'language':'ko-KR'
        }
    respond2 = requests.get(URL + path2 , params = params2).json()
    if movie_id != 0 :
        cast = []
        credit_cast = respond2.get('cast')
        for a in credit_cast :
            if a.get('cast_id')<10:
                cast.append(a.get('name'))
        
        crew = []
        credit_crew = respond2.get('crew')
        for a in credit_crew :
            if a.get('department') == 'Directing' :
                crew.append(a.get('name'))
        
        return {
            "cast" : cast ,
            "crew" : crew
        }
    else:
        0





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
