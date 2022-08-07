import requests

#ad5c1c30a5c68049f7bbc44e0db0c63a
#https://api.themoviedb.org/3/movie/76341?api_key=<<api_key>>

def popular_count():
    pass
    basic_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'

    params = {
    'api_key' : 'ad5c1c30a5c68049f7bbc44e0db0c63a',
    'language': 'ko-Kr'
    }

    response = requests.get(basic_URL+path,params=params).json()
    return len(response.get('results'))



 # 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
   popular 영화목록의 개수 반환
    """
    print(popular_count())
#     # 20
