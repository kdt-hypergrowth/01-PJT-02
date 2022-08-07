import requests
from pprint import pprint
import requests
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv('api_key')



def recommendation(title):
    URL ='https://api.themoviedb.org/3/'
    
        
    path1 = 'search/movie'
    params1 ={
            'api_key':api_key ,
            'query' : title,
            'language':'ko-KR'
        } 
    response1 = requests.get(URL + path1 , params = params1).json()
    movie_search = response1.get('results')
    if movie_search == []:
        movie_id = 0
    else:
     movie_id =  movie_search[0].get('id')
    
    path2 = f'movie/{movie_id}/recommendations'
    params2 = {
        'api_key':'c85b6b9693031d62b3c34274ee1a726a' ,
        'language':'ko-KR'
    } 
    result = []
    response2 = requests.get(URL + path2 , params = params2).json()
    if movie_id != 0:
      for a in response2.get('results'):
       result.append(a.get('title'))
      return result
    else:
        0

    
    




# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
