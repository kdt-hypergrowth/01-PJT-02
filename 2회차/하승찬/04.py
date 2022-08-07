import requests
from pprint import pprint


def recommendation(title):
    pass 
    # 여기에 코드를 작성합니다.  
        
    n = input()
    #추천영화목록 GET/movie/{movie_id}/recommendations   
    sbase_ulr ='https://api.themoviedb.org/3'
    spath = '/search/movie'   
    sparams = {
      'api_key' : '9c84ae21c51581335eb9aca74793ddb9',
      'language' : 'ko-KR',
      'query'    :  f'{n}'
    }

    sresponse =requests.get(sbase_ulr + spath,params=sparams)

    data= sresponse.json().get('results')
    movie_id = data[0].get('id')

    # print(movie_id)
    # 영화추천 코드
    base_ulr ='https://api.themoviedb.org/3'
    path = (f'/movie/{movie_id}/recommendations')
    params = {
      'api_key' : '9c84ae21c51581335eb9aca74793ddb9',
      'language' : 'ko-KR'
    }

    response =requests.get(base_ulr + path,params=params)



    recomend = response.json().get('results')

    recomend_list= []
    for i in range(len(recomend)):
      recomend_list.append((recomend[i].get('title')))
    


    print(recomend_list)


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
