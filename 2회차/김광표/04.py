import requests
from pprint import pprint


def recommendation(title):
    try :
        base_url = 'https://api.themoviedb.org/3'  
        path = '/search/movie'
        params = {
            'api_key' : '01d26c653a736a722edb8d872c129e3d',
            'language': 'ko-KR',
            'query' : title
            } 
        resp = requests.get(base_url+path, params=params).json()['results'] #우선 title을 검색 한다
        movie_id = resp[0]['id'] #검색 결과로부터 id 값을 가져온다.

        path = f'/movie/{movie_id}/recommendations' #id로 추천영화를 가져온다.
        params = {
            'api_key' : '01d26c653a736a722edb8d872c129e3d',
            'language': 'ko-KR'
            }

        resp = requests.get(base_url+path, params=params).json()['results']
        recommend_movies = []
        for i in resp : #추천영화들의 title을 저장한다.
            recommend_movies.append(i['title'])
        if recommend_movies == [] :
            recommend_movies = '추천 영화가 없습니다' #추천 영화가 없을 시 출력한다.
    except : pass #검색 할 수 없는 영화일시 예외로 pass한다.
    else : return recommend_movies
    
if __name__ == '__main__':
    
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
