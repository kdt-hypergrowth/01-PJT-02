import requests


def popular_count(): 
  
    BASE_URL = 'https://api.themoviedb.org/3' # api 불러올 URL
    path = '/movie/popular' # URL 추가/ 원하는 정보를 가져오기 위함
    params = {
        'api_key' : '801b2f9c7a6d8dce6f3bd7f807c9ffc5', # 내 인증 정보나, 원하는 언어, 원하는 정보 등 세부 사항을 기록
        'language' : 'ko-KR'
    }

    response = requests.get(BASE_URL+path, params=params).json() # requests 받아오기 .json 딕셔너리 파일로
    return len(response.get('results')) # requests 받아온 딕셔너리의 results의 길이 반환 # 20


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    20
