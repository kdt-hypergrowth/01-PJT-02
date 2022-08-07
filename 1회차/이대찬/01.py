from urllib import response
import requests


def popular_count():
    #0de00acda6081b7131fa382c50d91123
    URL = 'https://api.themoviedb.org/3/movie/popular'
    params = {
        'api_key' : '0de00acda6081b7131fa382c50d91123',
        'language' : 'ko-KR'
        
    }
    response = requests.get(URL, params=params).json()
    a = len(response.get('results'))
    return a
    
    
    
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
