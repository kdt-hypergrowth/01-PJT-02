import requests
from pprint import pprint


def recommendation(title):
    pass 
    # 여기에 코드를 작성합니다.  
    try:
        URL = 'https://api.themoviedb.org/3'
        movie = '/search/movie'
        params = { 'api_key' : '896988be1c1bb3801b7d75f69bd7b9a5', 'language' : 'ko-KR', 'query' : title}
        result = requests.get(URL+movie, params = params).json()
        a = result['results']
        movi = a[0]['id'] # 입력값의 id번호 찾기

        movie2 = f'/movie/{movi}/recommendations' #id 번호를 입력하여 주소로 등록
        params = { 'api_key' : '896988be1c1bb3801b7d75f69bd7b9a5', 'language' : 'ko-KR'}
        result2 = requests.get(URL+movie2, params = params).json()
        cnt = result2['results']
        title_list = []
        for i in range(len(cnt)):
            title_list.append(cnt[i]['original_title']) # 영화 이름만 title_list 에 추가
        return title_list # 반환값, 추천 영화가 없을 경우 [] 반환
    except IndexError:
        return None # 오류 날시 None 출력

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
