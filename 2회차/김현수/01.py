# 0f810078345847f7d4b6930619626f55
# https://api.themoviedb.org/3/movie/550?api_key=0f810078345847f7d4b6930619626f55
# 01. 인기 영화 조회

import requests

def popular_count():

    base_url = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
    'api_key': '0f810078345847f7d4b6930619626f55', #API값 정의
    'language': 'ko-KR'
    }
    response = requests.get(base_url + path, params = params).json() #url과 API값을 이용하여 요청-> json문서화 해줘 
    results = response['results'] #받은값에서 결과 딕셔너리값만 추출
    
    return  len(results) #결과 딕셔너리에 있는 변수갯수 알려줘

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count()) #결과 딕셔너리에 있는 변수갯수 return값으로 받아서 출력
    # 20