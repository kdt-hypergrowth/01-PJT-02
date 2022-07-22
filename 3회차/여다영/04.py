#04. 영화 조회 및 추천 영화 조회

#- 영화 제목으로 검색을 하여 추천 영화 목록을 출력합니다.
#- requests 라이브러리를 활용하여 TMDB에서 영화제목으로 영화를 검색(Search Movies)합니다.
#- 응답 받은 결과 중 첫번째 영화의 id 값을 활용하여 TMDB에서 추천 영화 목록(Get Recommendations)을 가져옵니다.
#- 추천 영화 목록을 리스트로 반환하는 함수를 작성합니다.

### 결과 예시
#**요청 시점에 따라 다른 결과가 나올 수가 있습니다.**
#["조커", "1917", "조조 래빗", "원스 어폰 어 타임 인… 할리우드", "... 생략" ,"펄프픽션"]

#api_key : f4d88a36cfb682b86111c15f97a34324
#https://api.themoviedb.org/3/movie/550?api_key=f4d88a36cfb682b86111c15f97a34324

import requests
from pprint import pprint


def recommendation(title):
    pass 
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
