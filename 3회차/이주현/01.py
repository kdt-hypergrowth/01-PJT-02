import requests
from pprint import pprint


def popular_count():
    
# 여기에 코드를 작성합니다.  
    BASE_URL = 'https://api.themoviedb.org/3'  # 이 URL에서 데이터를 가져옴
    path = '/movie/popular'                     # 가져올 세부 경로
    params = {
    'api_key' :'bc8f8f1749168f795addaf61d9561f9c',  # 권한을 가진 키, 한글로 가져옴
          'language':'ko-KR'
          }
    # URL + 세부경로 + 권한 으로 .json으로 결과를 가져옴 
    response = requests.get(BASE_URL+path,params = params).json().get('results')
    return len(response)
   
    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
   
    # 20











