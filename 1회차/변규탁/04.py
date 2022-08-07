import requests
from pprint import pprint

    
def recommendation(title):
    url = 'https://api.themoviedb.org/3'
    path1 = '/search/movie'
    params = {
        'api_key': '26eaac93f79c23ac640e6c7c91fb93af',
        'language': 'ko-KR',
        'query' : title
    }

    movie_data = requests.get(url+path1, params=params).json()
    
    if movie_data.get('results'):
        movieid = movie_data.get('results')[0].get('id')
    else:
        movieid = None
        
    movie_id = movieid
    path2 = f'/movie/{movie_id}/recommendations'

    movie_recommend = requests.get(url+path2, params=params).json()
    
    movie_recommend_list = []
    
    if movie_recommend.get('results') == None:
        return None

    for movie in movie_recommend.get('results'):
        if movie == None:
            movie_recommend_list = None
        else:
            movie_recommend_list.append(movie.get('title'))

    return movie_recommend_list  


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
