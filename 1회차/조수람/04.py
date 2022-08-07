import os
import requests
from pprint import pprint
from dotenv import load_dotenv


def recommendation(title):

##########################################################################################
# 1. 기본 영화 설정
##########################################################################################
    load_dotenv()
    api_key = os.getenv('api_key')
    
    
    print(f"'{title}' 관련 추천 영화")
    query = f"query={title}"

##########################################################################################
# 2. title로 받은 영화의 id 확인
##########################################################################################

    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&{query}" #키워드(Query)를 통해, 특정 영화 정보 서치

    response = requests.get(url).json() 
    # pprint(response)

    movie_list = response['results']
    movie_id_list = []

    for i in range(len(movie_list)):
        if 'id' in movie_list[i]:  
            movie_id_list.append(movie_list[i]['id']) #movie_id['id'] 로는 오류 발생

    print(f"movie_id_list: {movie_id_list}, type: {type(movie_id_list)}, len: {len(movie_id_list)}")

##########################################################################################
# 3. 영화 id 기준으로 추천 영화 목록 확인
##########################################################################################

    movie_name_list = []

    for movie_id in movie_id_list:
        # 키워드(Query)를 통해, 특정 영화 정보 서치
        # &language=ko 으로 한국어 검색 결과 확인
        url_2 = f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={api_key}&language=ko"
        response_2 = requests.get(url_2).json() 

        movie_list_2 = response_2['results']

    # pprint(f"movie_list_2: {movie_list_2}, type: {type(movie_list_2)}, len: {len(movie_list_2)}")
 
        for i in range(len(movie_list_2)):                
            if 'title' in movie_list_2[i]:     
                movie_name_list.append(movie_list_2[i]['title'])

    return movie_name_list



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """

    pprint(recommendation('기생충'))
    # # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # # []
    pprint(recommendation('검색할 수 없는 영화'))
    # # None
