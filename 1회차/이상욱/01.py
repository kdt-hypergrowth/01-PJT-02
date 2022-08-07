# 27ff99b8111fb8b63fae9898cd9b455a
# 27ff99b8111fb8b63fae9898cd9b455a
# https://api.themoviedb.org/3
import requests


def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
    base_url = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key' : '27ff99b8111fb8b63fae9898cd9b455a',
        'language' : 'ko-KR'
    }

    res=requests.get(base_url+path,params=params).json()
    data = res
    result = (len(data['results']))

    return result
    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
