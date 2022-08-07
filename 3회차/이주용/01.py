import requests

def popular_count():
    params = {
        'api_key' : '',
        'language' : 'ko-KR'
    }
    base_url = 'https://api.themoviedb.org/3'
    popular_url = '/movie/popular'
    response = requests.get(base_url + popular_url, params=params).json()
    return len(response.get('results'))

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
