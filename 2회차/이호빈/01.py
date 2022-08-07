import requests
#57289526949f876f1e243aee06612c5f

def popular_count():
    

    url = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': '57289526949f876f1e243aee06612c5f',
        'language': 'ko-KR'
    }
    
    response = requests.get(url + path, params=params).json()
    
    return len(response["results"])

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
