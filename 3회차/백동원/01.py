import requests
from pprint import pprint
# 344b9a7b0867ea18b1b9d6356fb7a1f0
def popular_count():
    pass 
    URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': '344b9a7b0867ea18b1b9d6356fb7a1f0',
        'language': 'ko-KR'
    }
    response = requests.get(URL+path, params = params).json()
    popular_list = response.get('results')
    name_list = []
    for a in popular_list:
        name_list.append(a.get('title'))
    print(len(name_list))

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
