import requests
from pprint import pprint
api_key = "17d99d001f6c99dd0c99035720f60646"

def recommendation(title):
    pass 
    # 여기에 코드를 작성합니다.
    try :
        searched_movie = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&language=ko-KR&query={title}&page=1"
        res = requests.get(searched_movie).json()
        resResult = res['results']
        movie_id=resResult[0]['id']
        recommanded_movie = f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={api_key}&language=koKR&page=1"
        rmd = (requests.get(recommanded_movie)).json()
        rmd_result = rmd['results']
        title_list = []
        for i in rmd_result:
            title_list.append(i['title'])
        return title_list
    except:
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
