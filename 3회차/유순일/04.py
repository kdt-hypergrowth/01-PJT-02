import requests
from pprint import pprint

def recommendation(title):
    BASE_URL = 'https://api.themoviedb.org/3'                   # title을 통해서 id 검색해야하기에
    path = '/search/movie'                                      # query : title이라는 매개변수를 추가하고
    params = {                                                  # get을 이용해서 정보 얻어옴.
        'api_key': '167e7ed92eefe4e7dd569b558d9f2e36',
        'language': 'ko-KR',
        'query': title
    }
    res = requests.get(BASE_URL+path, params=params).json() 
   
    result = []                                                 # return에서 result로 리스트를 받아와야함.
    if res['results']:                                          # json에서 resutls 정보 받아옴.
        movie_id = res['results'][0]['id']
        path = f'/movie/{movie_id}/recommendations'             # movie_id라는 매개변수를 설정.

        params = {
            'api_key': 'b730b79937fc4c4e8a1d72531451f76b',
            'language': 'ko-KR',
            'movie_id': movie_id                                # url에 매개변수 movie_id가 들어가기에 매개변수에 추가.
        }
        res = requests.get(BASE_URL+path, params=params).json()
        if res['results']:
            for i in res['results']:                            # results 요소중에 title만 result에 추가.
                result.append(i['title'])
        return result
    else:
        return None                                             # 없으면 None 호출.


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
