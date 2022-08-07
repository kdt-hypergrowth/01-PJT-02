import requests


def popular_count():  
    api_key = 'a709df78a1a09780128430e580888cb9'
    
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page=1'
    response = requests.get(url).json()
    data = response['results']
    return len(data)
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
