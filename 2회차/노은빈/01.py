import requests


def popular_count():
    # 여기에 코드를 작성합니다.  
    base_url = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key' : '8b431f95b8d1aca3b694e017ecd9c4fb'
    }

    response = requests.get(base_url + path, params=params).json()

    return len(response['results'])  #인기 영화 개수 조회

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
