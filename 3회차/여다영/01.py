#01. 인기 영화 조회

#- 인기 영화 목록의 개수를 출력합니다.
#- requests 라이브러리를 활용하여 TMDB에서 현재 인기 있는 영화 목록(Get Populations) 데이터를 요청합니다.
#- 응답 받은 데이터 영화 개수를 반환하는 함수를 작성합니다.

#결과 예시
#20

#api_key : f4d88a36cfb682b86111c15f97a34324
#https://api.themoviedb.org/3/movie/550?api_key=f4d88a36cfb682b86111c15f97a34324

import requests


def popular_count():
    pass 
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': 'f4d88a36cfb682b86111c15f97a34324'
    }

    response = requests.get(BASE_URL + path, params = params).json()
    results = response.get('results') #list 형식이다.

    return len(results)



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
