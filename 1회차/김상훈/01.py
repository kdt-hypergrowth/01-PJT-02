import requests
from pprint import pprint

# 2. 특정 조건에 맞는 영화 출력
def  popular_count():
    pass
    
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': '',
        'language': 'ko-KR'
}
    response = requests.get(BASE_URL+path, params=params).json()
    return(len(response['results'])) # response -> results 추출, 길이 반환


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20