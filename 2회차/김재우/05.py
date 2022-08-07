import requests
from pprint import pprint


def credits(title):
    BASE_URL = 'https://api.themoviedb.org/3' # api 정보 가져올 주소!
    path = '/search/movie' # search 검색하는 세부 주소! 
    params = {
        'api_key' : '801b2f9c7a6d8dce6f3bd7f807c9ffc5', # 내 인증키나 세부 정보!
        'language' : 'ko-KR',
        'query' : title # title을 검색할 것!
    }
    response = requests.get(BASE_URL+path, params=params).json() # requests 받아옴

    if response['results']: # 만약에! response에 result 가 있다면 
        movie_id = response['results'][0]['id'] # movie_id 는 requests 받은 results의 첫번째 영화 id 를 가져온다!
        path2 = f'/movie/{movie_id}/credits' # 2번째 세부 주소! credit을 id를 사용해서 불러온다
        params2 = {
            'api_key' : '801b2f9c7a6d8dce6f3bd7f807c9ffc5',  # 내 인증키나 세부 정보 !
            'language' : 'ko-KR',
        }
        response2 = requests.get(BASE_URL+path2, params=params2).json() # 2번쨰 requests
        
        result_dict ={'cast':[], 'crew':[]} # dic 딕셔너리 저장소 만들기 ! cast 와 crew가 필요 {} 딕셔너리 안에 [] 생성

        for i in response2['cast']: # 반복문 이용 i에 'cast' 데이터 저장
            if i['cast_id'] < 10: # cast_id 가 10 이하인 데이터라면
                result_dict['cast'].append(i['name']) # 내가 만든 딕셔너리 저장소 'cast'에 append! 무엇을? = i 데이터의 'name'을!
        
        for j in response2['crew']: # 반복문 이용 i에 'crew' 데이터 저장
            if j['department'] == 'Directing' : # 데이터가 저장된 j에 department가 Directing 인 데이터만!
                result_dict['crew'].append(j['name']) # 내가 만든 딕셔너리 저장소 'crew'에 append! 무엇을? = j 데이터의 'name'을!

        return result_dict # 딕셔너리 저장소를 반환해준다!
    
    else:
        return None # 만약에 아무것도 포함되지 않았다. (이름이 없는 경우! ) None 을 반환해준다!!

    


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
