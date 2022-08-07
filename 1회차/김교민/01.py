#42259abc0f3225655eba5deb9d51f7f3
#https://api.themoviedb.org/3/movie/550?api_key=42259abc0f3225655eba5deb9d51f7f3
import requests


def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
    url = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': '42259abc0f3225655eba5deb9d51f7f3',
        'language': 'ko-KR'
    }
    re = requests.get(url+path, params=params).json()
    return len(re['results']) #가져온 데이터의 'results'리스트의 크기를 알려주는 len함수 활용

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
