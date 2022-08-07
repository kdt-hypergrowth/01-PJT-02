import requests


def popular_count():
    pass 
    # 여기에 코드를 작성합니다. 

    BASE_URL = 'https://api.themoviedb.org/3/'
    path = 'movie/popular'
    params = {
    'api_key': '50dcaaa56233584245e4cb9685b3a049',
    'language': 'ko_KR'
    }
    response = requests.get(BASE_URL+path, params=params).json()
    result = response.get('results')
    return len(result)

    
#아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
