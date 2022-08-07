import requests
from pprint import pprint
api_key = "17d99d001f6c99dd0c99035720f60646"

def credits(title):
    pass 
    # 여기에 코드를 작성합니다.  
    searched_movie = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&language=ko-KR&query={title}&page=1"
    res = requests.get(searched_movie).json()
    resResult = res['results']
    credit_id=resResult[0]['id']
    credit_search = f"https://api.themoviedb.org/3/credit/{credit_id}?api_key={api_key}"
    crd = requests.get(credit_search).json()
    pprint(crd)
credits("대부")
# 아래의 코드는 수정하지 않습니다.
# if __name__ == '__main__':
#     """
#     제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
#     영화 id 검색에 실패할 경우 None을 반환
#     """
#     pprint(credits('기생충'))
#     # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
#     pprint(credits('검색할 수 없는 영화'))
#     # None
