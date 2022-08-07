import requests


def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
    URL = 'https://api.themoviedb.org/3'
    movie = '/movie/popular'
    params = { 'api_key' : '896988be1c1bb3801b7d75f69bd7b9a5', 'language' : 'ko-KR'}
    result = requests.get(URL+movie, params = params).json()
    data = result['results']
    cnt = 0
    for i in data:
        cnt += 1 # 영화 갯수에 따라 카운트 + 1
    return cnt
 
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
