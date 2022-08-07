# - 영화 제목으로 검색을 하여 추천 영화 목록을 출력합니다.
# - requests 라이브러리를 활용하여 TMDB에서 영화제목으로 영화를 검색(Search Movies)합니다.
# - 응답 받은 결과 중 첫번째 영화의 id 값을 활용하여 TMDB에서 추천 영화 목록(Get Recommendations)을 가져옵니다.
# - 추천 영화 목록을 리스트로 반환하는 함수를 작성합니다

import requests
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()
MV_API_KEY = os. environ.get("MV_API_KEY")

#search하나 rcmd하나 해서 2개의 결과가 필요
def recommendation(title):

    # 여기에 코드를 작성합니다.  
    MV_URL = 'https://api.themoviedb.org/3'   
    path1 = '/search/movie'                   
    search_URL = MV_URL + path1
    params = {
            'api_key': MV_API_KEY  ,     
            'language': 'ko-KR' ,
            'query' : title                        
        }
    rsp = requests.get(search_URL, params=params).json().get('results')
   
    if len(rsp) == 0:
        return None  #검색 결과가 없다면 none반환

    #검색한 영화는 id로 추천 목록
    MV_URL = 'https://api.themoviedb.org/3'   
    path2 ='/movie/'+str(rsp[0].get('id'))+'/recommendations'                  
    rcmd_URL = MV_URL + path2
    params = {
        'api_key': MV_API_KEY  ,     
        'language': 'ko-KR'                        
     }

    rcmd = []
    rsp2 = requests.get(rcmd_URL, params=params).json().get('results')
   
    for i in rsp2:
        rcmd.append(i.get('title'))
    return rcmd


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
