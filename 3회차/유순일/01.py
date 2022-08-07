import requests


def popular_count():                                                            # popular_count 함수 선언
    BASE_URL = 'https://api.themoviedb.org/3'                                   # API 가져와야하는데 고정된 url이라 BASE_URL로 설정.
    path = '/movie/popular'                                                     # path부분만 배너에 따라 바뀌기에 따로 path 설정. 
    params = {                                                                  # api불러올 때 필요한 매개변수.
        'api_key': '167e7ed92eefe4e7dd569b558d9f2e36',
        'language': 'ko-KR'
    }                                 #매개변수
    res = requests.get(BASE_URL+path, params=params).json().get('results')      # popular_count()함수의 핵심 작동코드.
    # 결국, get()에서 https://api.themoviedb.org/3/movie/popular?api_key=167e7ed92eefe4e7dd569b558d9f2e36&language=ko-KR api호출 -> json형태로 정리 -> results 값만 호출
    # results(dictionary)에 영화들의 내용들이 담겨있기에, 그 안의 요소 개수만 파악하면 영화를 몇개 불러 올 수 있는지 파악 가능. 그래서 위와 같은 코드 작성.
    
    return len(res)                                                             # res 코드에서 작동 후 results의 요소의 개수만 파악하기 위해
                                                                                # len(res)형태로 최종적으로 함수 호출.

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    print(popular_count())                                                      # 함수 호출
    # 20
