from dotenv import load_dotenv
import os
import requests
from pprint import pprint


def recommendation(title):
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
    if len (response.get('results')) > 0:
        movie_name_id =  response.get('results')[0]['id']
        
    else:
        movie_name_id =  None

    path2 = f'/movie/{movie_name_id}/recommendations'
    response2 = requests.get(URL + path2, params = params).json()

    ans = response2.get('results')
    ans_list=[]
    if ans != None:

        for i in range(len(ans)):
            ans_list.append(  ans[i].get('title')   )
        
        return ans_list

    else:
        return None



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
