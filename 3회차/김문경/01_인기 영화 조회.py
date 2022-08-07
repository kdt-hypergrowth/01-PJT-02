
#* 인기 영화 목록의 개수를 출력합니다.
#* requests 라이브러리를 활용하여 TMDB에서 현재 인기 있는 영화 목록(Get Populations) 데이터를 요청합니다.
#* 응답 받은 데이터 영화 개수를 반환하는 함수를 작성합니다.

import requests
BASE_URL = 'https://api.themoviedb.org/3'
# 기본 BASE_URL, 영화 정보 사이트
path = '/movie/now_playing?api_key=617e47b888d4519a585f9f4cd8bbab6e&language=en-US&page=1'
# 그 뒤에 붙여줄 경로, 현재 인기 있는 영화 목록 데이터를 요청해야하니 'now_playing' 파트 들어가서 코드 복붙
# api_key는 내꺼로 해서 저장, 뒤에 language나 page는 옵션!
URL = BASE_URL + path
def popular_count():
    response = requests.get(URL).json()
    # 내가 설정해둔 URL에서 json 파일 형식으로 담아온 것을 response에다 담기
    results = response['results']
    # 설정해둔 URL가면 json파일로 쭉 나오고 데이터 구조가 어떻게 형성돼있는지 한 눈에 알아볼 수 있다.
    # 그 데이터 구조를 보고 'results'라는 키에 영화 정보들이 담겨져있기 때문에 여기로 접근해서 카운트를 하자라고 생각 가능
    cnt = 0
    for i in results:
        cnt += 1
    return cnt

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
