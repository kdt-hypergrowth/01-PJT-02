import requests
from pprint import pprint


def popular_count():

def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
    import requests
    BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/popular'
params = {
    'api_key' : 'ae34f93c0dcff82c16eb8b18b5631edb',
    'language' : 'ko-KR'
}
response = requests.get(BASE_URL+path, params = params).json().get('results')
    return len(response)
    # 반복하여 이름 뽑기 now_playing 현재 개봉중인 
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    pprint(popular_count())
    # 20
