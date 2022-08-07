import requests


def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
    base_URL = 'https://api.themoviedb.org/3/'
    path = 'movie/popular'
    params = {
        'api_key' : '',
        'language' : 'ko-KR'
        }
    response = requests.get(base_URL+path, params=params)
    movie_dict = response.json()
    return len(movie_dict['results'])

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
