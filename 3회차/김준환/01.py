import requests


def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
    base_url = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': 'e2be94a1762b4b81af8b205d5e2bcb5f',
        'language': 'ko-KR'
    }
    response = requests.get(base_url+path, params=params).json()
    results = response['results']

    return len(results)


    #아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """   
    print(popular_count())
    #20