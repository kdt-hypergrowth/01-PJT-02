import requests
# 474c622ef9ff33b07a0bac17dd3e0ff2
# https://api.themoviedb.org/3/movie/76341?api_key=<<api_key>>

def popular_count():
    pass 
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
    'api_key': '474c622ef9ff33b07a0bac17dd3e0ff2',
    'language': 'ko-KR'
    }
    response = requests.get(BASE_URL+path, params = params)
    data = response.json()
    result = len(data['results'])
    
    return result
    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
