import requests


def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
    b_url = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
    'api_key': '21c47128f53c4a2d7c4e8584e6fad669',
    'language': 'ko-KR'
    }

    response = requests.get(b_url+path, params=params).json()
    return len(response.get('results'))

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20