# 문제04. 영화 조회 및 추천 영화 조회(Search Movies)
# 영화를 검색하고, 응답받은 결과 중 첫번째 영화id 값을 활용하여 추천 영화 목록(Get Recommendations) 가져옴
# 추천 영화 목록을 리스트로 반환
# 단, 영화가 검색되지 않을 경우 None을 반환하고, 추천 영화가 없을 경우 []을 반환

from ast import AsyncFunctionDef
import requests
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('api_key')


def recommendation(title):
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

        # 추천 영화 접속 URL 설정 및 movie_id 값 전달
        movie_id = movie_recom
        URL2 = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key=f76c49785033a7b6c167ccd0691c80e8&language=ko'

        # 요청 보내서 응답을 받음
        response2 = requests.get(URL2)

        # 응답 받은 데이터(json) 내 영화정보가 담긴 json 파일을 가져옴
        data2 = response2.json()

        # json 파일 중 영화제목만 추출 후 추천 영화 제목만 출력
        # 영화는 검색되나 추천영화가 없을 경우 [], 영화 검색이 되지 않으면 None
        movie_recom_subject = []

        for i in range(0, len(data2.get('results'))):
            movie_recom_subject.append(data2.get('results')[i].get('original_title'))
        return movie_recom_subject

    except:
        return None

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
