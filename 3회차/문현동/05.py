import os
import requests
from pprint import pprint
from dotenv import load_dotenv



def credits(title):
    
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
        
    if response.get("results"): # 만약 어떤 코드가 response.get("results") 라면, 아래 코드를 실행하고 /// 즉 response.get("results") 가 있다면 (?)
        
        movie_id = response.get("results")[0].get("id")
        
        credit_data = [] # 분류되지 않은 전체 제작 참여자들의 정보가 담긴 리스트 입니다.
        caster_data = []
        crew_data = []
        
        caster_name = [] # 어떤 기준으로 분류된 배우들의 이름이 담긴 리스트 입니다.
        crew_name = [] # 어떤 기준으로 분류된 스태프들의 이름이 담긴 리스트 입니다.
        
        get_credit_path = f"/movie/{movie_id}/credits"
        credit_data = requests.get(url = base_url + get_credit_path + f"?api_key={api_key}").json()
        
        # requests.get(url = base_url + credit_path + f"?api_key={api_key}").json().get('cast')
        # 이 것 자체가 리스트인데 append 를 하게 되면 리스트 안에 리스트를 집어넣는 모양이 된다.
        # extend 혹은 += 를 사용하여 리스트끼리 합쳐지게 만들어야 합니다.
        
        caster_data = credit_data.get("cast")
        crew_data = credit_data.get("crew")
        
        for cast in caster_data:
            if cast["cast_id"] < 10:
                caster_name.append(cast["name"])
        
        for crew in crew_data:
            if crew["department"] == "Directing":
                crew_name.append(crew["name"])
        
        return {"cast" : caster_name, "crew" : crew_name}
        
    else:
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
