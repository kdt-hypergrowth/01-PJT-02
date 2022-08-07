import requests

# https://api.themoviedb.org/3/movie/76341?api_key=<<api_key>>
# 143e53e7e83b57a0c8376b3020cd5051
def popular_count():
    # UMLMaket 클래스의 인스턴스 생성
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'

    params = {
        'api_key' : '143e53e7e83b57a0c8376b3020cd5051',
        'language': 'ko'
    }
    # url를 통해 서버에 요청해서 응답받고, json타입 데이터를 dictionary타입으로 바꿔 변수에 저장
    response = requests.get(BASE_URL+path, params=params).json() 
   # 총 페이지 수 확인
   # print(response)

    # results를 추츨해. 길이 반환
    return len(response['results'])
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
