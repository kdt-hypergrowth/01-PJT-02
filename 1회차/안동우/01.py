
import json
import requests
# 예 https://api.themoviedb.org/3/movie/550?api_key=
# 키 ee4e03d2e5481d6c59df596e0ff9fc6a
def popular_count():
    pass 
    
    base_URL='https://api.themoviedb.org/3'
    path= '/movie/popular'

    params = {

        'api_key':'ee4e03d2e5481d6c59df596e0ff9fc6a',
        'language': 'ko-KR'
    }

    a = requests.get(base_URL+path, params=params).json().get('results')
   
    
    return(len(a))
    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
