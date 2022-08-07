import requests
import json
from pprint import pprint

#https://api.themoviedb.org/3/get/search/movie




    
    
print(output_list)
    





def recommendation(title):
    params = {
       'api_key' : 'de3d5824ffe66b5d535f7edae4d285d6',
       'language' : 'ko',
    }

    base_url = 'https://api.themoviedb.org/3/search/movie?api_key=de3d5824ffe66b5d535f7edae4d285d6&language=ko&query='

    url = base_url+title

    res = requests.get(url,params=params).json()

    movie_id = res['results'][0]['id']


    url = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations'
    res = requests.get(url,params=params).json()

    output_list =[]
    for m in res['results']:
        output_list.append(m['original_title'])
        
    return output_list


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