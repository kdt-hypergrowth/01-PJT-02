from urllib import response
import requests


def popular_count():
    
    # 기본 api를 가져올 수 있는 주소
    BASIC_URL = 'https://api.themoviedb.org/3'
    # 인기영화 api 주소와 내 api 키입력
    path = '/movie/popular'
    params = {'api_key' : 'ec5782cbc602381ddeeedd23dcf585b9',
        'language' : 'ko',
        'region' : 'KR'
        }
   # request 요청한 걸 받아온다
    response = requests.get(BASIC_URL+path,params=params)
    # 응답 받은 response를 json을 입력해 딕셔너리로 바꿔준다
    data_dict = response.json()

            # results 길이 구하기
    return  len(data_dict['results'])

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
