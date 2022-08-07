import os
import requests
from dotenv import load_dotenv

def popular_count():
    
    load_dotenv(verbose = True)
    api_key = os.getenv('api_key')
    base_url = os.getenv('base_url')
    population_path = "/movie/popular"
    
    payload = {"api_key" : api_key,
            "language" : "ko-KR",
            "page" : 1}
    
    
    
    response = requests.get(url = base_url + population_path, params = payload).json()
        
    movie_title_list = []
    
    for movie_info in response.get("results"):
        movie_title_list.append(movie_info.get("title"))
    return len(movie_title_list)



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
