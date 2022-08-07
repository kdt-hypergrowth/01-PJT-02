# - 인기 영화 목록의 개수를 출력합니다.
# - requests 라이브러리를 활용하여 TMDB에서 현재 인기 있는 영화 목록(Get Populations) 데이터를 요청합니다.
# - 응답 받은 데이터 영화 개수를 반환하는 함수를 작성합니다.

import requests

def popular_count():
    URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': '66393cafe6777ee92a0cc513816794be',
        'language': 'ko-KR'
    }

    response = requests.get(URL+path, params=params).json()
    return len(response['results'])


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20


# # 8854669b886a6c07c12ea947bcc2311d
# # https://api.themoviedb.org/3/movie/76341?api_key=<<api_key>>
# import requests
# BASE_URL = 'https://api.themoviedb.org/3'
# path = '/movie/43261'
# # api_key 발급받아서 각자 키를 넣어주세요.
# params = {
#     'api_key': '',
#     'language': 'ko-KR'
# }

# response = requests.get(BASE_URL+path, params=params).json()
# print(response)