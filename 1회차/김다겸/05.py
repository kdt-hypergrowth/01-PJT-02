import requests
from pprint import pprint

# 제공된 영화 제목을 검색하여 해당 영화의 출연진(`cast`) 그리고 스태프(`crew`) 중 연출진으로 구성된 목록만을 출력합니다.
# requests 라이브러리를 활용하여 TMDB에서 영화제목으로 영화를 검색(Search Movies)합니다.
# 응답 받은 결과 중 첫번째 영화의 id 값을 활용하여 TMDB에서 해당 영화에 대한 출연진과 스태프 목록(Get Credits)을 가져옵니다.
# 출연진 중 `cast_id` 값이 `10 미만`인 출연진만 추출하고, 연출진은 부서(`department`)가 `Directing` 인 데이터만 추출합니다.
# `cast` 와 `directing` 으로 구성된 딕셔너리에 추출된 값을 리스트로 출력하는 함수를 작성합니다.

def credits(title):
    BASE_URL = 'https://api.themoviedb.org/3'
    search = '/search/movie'
    params = {
        'api_key' : '94ceed584568fa7a9113545f2e4291f5',
        'language' : 'ko-KR',
        'query' : title
    }
    # 영화 검색 BASE_URL에서 API request
    response = requests.get(BASE_URL+search, params=params)
    # 요청한 데이터를 json 형태로 가져온 후 'results'에 해당하는 값들을 저장
    movies = response.json().get('results')
    
    try:
        # title에 해당하는 검색 결과의 첫번째 데이터의 'id' 저장
        id = movies[0]['id']
        # 검색할 수 없는 영화이면 None 저장하도록 예외처리
    except:
        id = None

    credit1 = '/movie/'
    movie_id = str(id)
    credit2 = '/credits'
    params = {
            'api_key' : '94ceed584568fa7a9113545f2e4291f5',
            'language' : 'ko-KR'
        }

    # BASE_URL에서 해당 id에 맞는 스태프 목록 API request
    response = requests.get(BASE_URL+credit1+movie_id+credit2, params=params).json()

    # {'id': 496243, 'cast': [{'adult': False, 'gender': 2, 'id': 20738, 'known_for_department': 'Acting', 
    # 'name': 'Song Kang-ho', 'original_name': 'Song Kang-ho', 'popularity': 19.005, 'profile_path': '/dyWUKQlNyr7SUAjo58VZXvPODkr.jpg', 
    # 'cast_id': 0, 'character': 'Kim Ki-taek', 'credit_id': '5a4db31fc3a3683b82003a00', 'order': 0}, ...(생략)], 
    # 'crew': [{'adult': False, 'gender': 2, 'id': 21684, 'known_for_department': 'Directing', 'name': 'Bong Joon-ho', 
    # 'original_name': 'Bong Joon-ho', 'popularity': 6.52, 'profile_path': '/tKLJBqbdH6HFj2QxLA5o8Zk7IVs.jpg', 
    # 'credit_id': '5e86239298f1f10016ab4889', 'department': 'Writing', 'job': 'Screenplay'}, ...(생략)], 'id': 496243}
    
    # None으로 데이터가 넘어왔으면
    if movies == None:
        # None 출력
        return None

    # 'cast'와 'crew'에 빈 리스트 생성
    ans = {'cast':[], 'crew':[]}
    
    try:
        # response의 'cast'의 값에 반복문으로 접근
        for cast in response['cast']:
            # 만약 'cast_id'가 10보다 작으면
            if cast['cast_id'] < 10:
                # ans의 'cast' 키의 값에 cast의 'name' 추가
                ans['cast'].append(cast['name'])
        
        # response의 'crew'의 값에 반복문으로 접근
        for crew in response['crew']:
            # 만약 'department'가 'Directing'이면
            if crew['department'] == 'Directing':
                # ans의 'crew' 키의 값에 crew의 'name' 추가
                ans['crew'].append(crew['name'])
    # 'cast'에 KeyError가 발생하면 None으로 예외처리
    except:
        return None

    return ans


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    print(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    print(credits('검색할 수 없는 영화'))
    # None