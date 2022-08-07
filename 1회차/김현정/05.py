# 문제05. 출연진 및 연출진 데이터 조회
# 영화 제목을 검색하여 해당 영화의 출연진(cast) 그리고 스태프(crew) 중 연출진으로 구성된 목록만 출력

import requests
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('api_key')


def credits(title):
    pass 
    # 여기에 코드를 작성합니다.  
    # 영화 검색 접속 URL 설정
    URL1 = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&language=ko&query={title}'
    
    # 요청 보내서 응답을 받음
    response = requests.get(URL1)

    # 응답 받은 데이터(json) 내 영화정보가 담긴 json 파일을 가져옴
    data = response.json()

    # 제목에 해당하는 영화의 id 값을 변수에 저장, 없을 경우 except 구문을 통해 None 반환
    try:
        movie_recom = data.get('results')[0].get('id')

        # 출연진, 스태프 목록 가져오기
        movie_id = movie_recom
        URL2 = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=f76c49785033a7b6c167ccd0691c80e8&language=ko'

        # 요청 보내서 응답을 받음
        response2 = requests.get(URL2)

        # 응답 받은 데이터(json) 내 영화정보가 담긴 json 파일을 가져옴
        data2 = response2.json()

        # 출연진(cast)는 cast_id 10 미만인 데이터만 추출
        movie_cast = []
        for i in range(0, len(data2.get('cast'))):
            if data2.get('cast')[i].get('cast_id') < 10:
                movie_cast.append(data2.get('cast')[i].get('name'))
        
        # 연출진(crew)는 부서가 Directing인 데이터만 추출
        movie_crew = []
        for j in range(0, len(data2.get('crew'))):
            if data2.get('crew')[j].get('department') == 'Directing':
                movie_crew.append(data2.get('crew')[j].get('name'))

        # 출연진과 연출진을 담을 딕셔너리 선언 및 추출 리스트 Value값으로 삽입
        movie_total = {'cast' : movie_cast, 'crew' : movie_crew}

        return movie_total

    except:
        return None

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
