from urllib import response
import requests
from pprint import pprint


def recommendation(title):
    url = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': '57289526949f876f1e243aee06612c5f',
        'language': 'ko-KR',
        'query' : f'{title}'
    }
    rec_list = [] #결과값 담을 리스트
    response = requests.get(url + path, params = params).json()
    # 값이 존재하지 않으면 None 리턴
    if response.get('results') == []:
        return None
    else:
        # 첫번째 영화 id 뽑아낸다
        result_id = response.get('results')[0].get('id')
        url2 = f"/movie/{result_id}/recommendations"
        response2 = requests.get(url + url2, params = params).json()
        result_id_2 = response2.get('results')
        # 제목만 추출해서 list에 삽입
        for movie in result_id_2:
            rec_list.append(movie.get('title'))

        return rec_list
        



    




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
