import requests


def popular_count():
    pass 
    url = 'https://api.themoviedb.org/3'
    PATH = '/movie/popular'
    movie_info = {
    'api_key' : '',
    'language' : 'ko-KR'
    }

    response = requests.get(url+PATH, params=movie_info).json()

    ppmovie_list = response.get('results')

    cnt = 0
    for movie in ppmovie_list:
        cnt += 1
    return cnt 


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
