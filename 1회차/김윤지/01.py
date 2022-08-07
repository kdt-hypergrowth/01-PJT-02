# - 인기 영화 목록의 개수를 출력합니다.
# - requests 라이브러리를 활용하여 TMDB에서 현재 인기 있는 영화 목록(Get Populations) 데이터를 요청합니다.
# - 응답 받은 데이터 영화 개수를 반환하는 함수를 작성합니다.


import requests    # 모듈을 불러온다.
import os
from dotenv import load_dotenv

load_dotenv()
MV_API_KEY = os. environ.get("MV_API_KEY")


def popular_count():

    # 여기에 코드를 작성합니다. 
    MV_URL = 'https://api.themoviedb.org/3'   #URL로 요청을 보내서
    path = '/movie/popular'                   

    params = {
        'api_key': MV_API_KEY,  #내 APi key
        'language': 'ko-KR'     #언어변경                
 }

    response = requests.get(MV_URL+path, params=params).json()
    #응답 받은 값을 가져온다.
    return len(response["results"]) #함수리턴하기

    



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
