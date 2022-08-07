import requests


def popular_count():
    base_url = 'https://api.themoviedb.org/3/movie/popular'
    params = {
        'api_key': 'f25f9449dadd6f959e63b7b058966cea',
        'language': 'ko-KR'
    }
    
    response = requests.get(base_url, params=params).json()
    return len(response['results'])
    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20