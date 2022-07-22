import requests


def popular_count():
    url = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key':'db73cdf92f64511f998356227c82b682',
        'language':'ko-KR'
    }
    response=requests.get(url+path, params=params).json().get('results')
    return len(response)


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
