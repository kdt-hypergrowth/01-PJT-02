from dotenv import load_dotenv
import os
import requests
from pprint import pprint


def credits(title):
    pass 
    # 여기에 코드를 작성합니다.  
    load_dotenv()

    key = os.getenv("KEY")
    
    params = {
        "api_key": key,
        "query": title,
        "language": "ko-kr"
    }

    baseURL = "https://api.themoviedb.org/3"
    specificURL = "/search/movie"
    response = requests.get(baseURL + specificURL, params=params).json()

    if response["results"]:
        movie_id = response["results"][0]['id']
        specificURL = f"/movie/{movie_id}/credits"
        
        if "query" in params:
            del params["query"]
        
        response = requests.get(baseURL + specificURL, params=params).json()

        if response["cast"] and response["crew"]:
            result = {}
            cast = list(map(lambda x: x["original_name"], filter(lambda x: x["cast_id"] < 10, response["cast"])))
            crew = list(map(lambda x: x["original_name"], filter(lambda x: x["department"] == "Directing", response["crew"])))
            result["cast"] = cast
            result["crew"] = crew
        else:
            result = []

    else:
        result = None

    return result

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
