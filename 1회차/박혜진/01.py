import requests


def popular_count():

    url = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key' : '09a613146a968647b2f3039070613000',
        'language' : 'ko-KR'
    }

    response = requests.get(url + path, params=params).json()
    results = response['results']

    movie_count = 0

    for i in results :
        if i['id'] != 0 :
            movie_count += 1

    return movie_count


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
