import requests


def popular_count():
    base_url = 'https://api.themoviedb.org/3'
    path = '/movie/popular'

    params = {
        'api_key' : '09d0041de8747ddc735a2981381ae949',
        'language' : 'ko',
    }
    res = requests.get(base_url+path, params=params)
    data = res.json()
    result = len(data['results'])
    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    #popular 영화목록의 개수 반환
    print(popular_count())
    # 20
