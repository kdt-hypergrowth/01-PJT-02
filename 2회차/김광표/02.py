import requests
from pprint import pprint


def vote_average_movies():
    base_url = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
    'api_key' : '01d26c653a736a722edb8d872c129e3d',
    'language': 'ko-KR'
    }
    resp = requests.get(base_url+path, params=params).json()['results']
    movies_pop = []
    for i in resp :

        if int(i['vote_average']) >= 8 :
            movies_pop.append(i)
    return movies_pop
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    pprint(vote_average_movies())

