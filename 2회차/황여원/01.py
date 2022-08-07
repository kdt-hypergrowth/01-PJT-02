# d1c47d9288b0354c3305720bd5e426e7
# https://api.themoviedb.org/3/movie/76341?api_key=<<api_key>>
import requests

def popular_count():
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
         'api_key': 'd1c47d9288b0354c3305720bd5e426e7',
         'language' : 'ko-KR'        
     }

    response = requests.get(BASE_URL+path, params=params).json()
    movie = response.get('results')
    # return response
    cnt = 0
    for i in movie : 
        cnt += 1 
    return cnt


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20

