import requests


def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
    URL = 'https://api.themoviedb.org/3'
    popular_movie = '/movie/popular'
    params = {
        'api_key' : '7b4d11acc694dae76c459794c57dd6c4',
        'language' : 'ko-KR'
    }
    response = requests.get(URL+popular_movie, params=params).json()
    results = response.get('results')
    popular = []
    for i in results :
        popular.append(i['title'])
    return len(popular)
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
