from asyncio.proactor_events import _ProactorDuplexPipeTransport
import requests


def popular_count():
    pass
    
    # 여기에 코드를 작성합니다.  
    return (response.get('results'))
import requests

Base_URL = "https://api.themoviedb.org/3/"
path = 'movie/popular/'
params = {
    'api_key': 'c88039a3ac8630f316e088cdecaae57a',
    'language': 'ko-KR'}

response =requests.get(Base_URL+path, params=params).json()



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
