import requests
from pprint import pprint


def ranking():
    base_url = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key' : '01d26c653a736a722edb8d872c129e3d',
        'language': 'ko-KR'
    }


    resp = requests.get(base_url+path, params=params).json()['results']
    movie_ranking = sorted(resp, key=lambda res : (res['vote_average']), reverse= True)
    # sorted를 이용해 vote average의 값의 내림차순으로 정렬
    return movie_ranking[0:5] # 1~5위의 영화만 반환

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    pprint(ranking())
