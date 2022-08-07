import os
import requests
from pprint import pprint
from dotenv import load_dotenv



def recommendation(title):
    
    load_dotenv(verbose = True)
    api_key = os.getenv('api_key')
    base_url = os.getenv('base_url')
    movie_path = "/search/movie"
    
    payload =\
    {
        "api_key" : api_key,
        "language" : "ko-KR",
        "query" : title
    }
    response = requests.get(url = base_url + movie_path, params = payload).json()
    
    ### print(response)
    
    if response.get("results"): # 만약 어떤 코드가 response.get("results") 라면, 아래 코드를 실행하고 /// 즉 response.get("results") 가 있다면 (?)
        
        movie_id = response.get("results")[0].get("id")
        reco_list = [] # 추천 영화들 제목이 들어가는 리스트
        
        get_recommendations_path = f"/movie/{movie_id}/recommendations" # 변경된 path 를 통해 추천 영화목록을 가져옵니다.
        response_recommendations = requests.get(url = base_url + get_recommendations_path + f"?api_key={api_key}&language=ko-KR").json()
        
        for reco_movies in response_recommendations.get("results"):
            reco_list.append(reco_movies.get("title"))
        
        return reco_list
        
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
