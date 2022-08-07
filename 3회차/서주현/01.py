import requests
import pprint

def popular_count():
    
    # API_key = '85bedf36756745d573166cfee3a12aa5'
    URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key' : '85bedf36756745d573166cfee3a12aa5'

    }
    response = requests.get(url = URL+path, params = params).json()
    cnt = 0
    
    for i in response['results'] :
        cnt  += 1
    # pp = pprint.PrettyPrinter()

    # pp.pprint(response)
    return cnt

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
