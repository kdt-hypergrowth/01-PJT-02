import requests


def popular_count():

    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    # api_key 발급받아서 각자 키를 넣어주세요.
    params = {
        'api_key': '23dbc507a8ed3160e9d5d6ac981da9b4',
        'language': 'ko-KR'
    }    

    response = requests.get(BASE_URL+path, params=params).json()

    a = response.get('results')
    cnt = 0
    for b in a:
        cnt += 1

    return cnt 
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
