import requests

def popular_count():
    url = 'https://api.themoviedb.org/3'
    path='/movie/popular'

    params = {
        'api_key': '3d086799f6ddf19a461e5ed8f4712adf',
        'language': 'ko-KR'
    }

    response = requests.get(url + path, params=params).json()
    data = response.get('results')
    return len(data)
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
