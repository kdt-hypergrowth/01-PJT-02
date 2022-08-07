import requests

def popular_count():

    base_url = 'https://api.themoviedb.org/3' # url 설정
    path = '/movie/popular' #인기영화
    params = {
    'api_key' : '01d26c653a736a722edb8d872c129e3d',
    'language': 'ko-KR', # api key 설정, 언어설정
    }
    resp = requests.get(base_url+path, params=params).json()['results'] #인기영화를 불러옴
    return len(resp) #인기영화의 개수를 반환


if __name__ == '__main__':
    print(popular_count())

