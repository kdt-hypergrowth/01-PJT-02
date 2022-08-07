import requests
from pprint import pprint


def search(title): 
    # 여기에 코드를 작성합니다.  
    
    # 다른분의 코드를 가져왔지만.. 아직 이해를 하지 못한 상황
    URL = 'https://api.themoviedb.org/3'
    path = '/search/movie' 
    params = {
        'api_key': '3d086799f6ddf19a461e5ed8f4712adf',
        'language': 'ko-KR',
        'query': f'{title}'
    }
    response = requests.get(URL + path, params = params).json().get('results') 
                                                                                
    for i in range(len(response)): 
        return response[i].get('id')

def credits(title):
    movie_id = search(title)   
    URL = 'https://api.themoviedb.org/3'
    path=f'/movie/{movie_id}/credits'
    params = {
        'api_key': '3d086799f6ddf19a461e5ed8f4712adf',
        'language': 'ko-KR',
        'query': f'{title}'
    }
    if movie_id == None:     
        return None 

   
    response1 = requests.get(URL + path, params=params).json().get('cast') 
    response2 = requests.get(URL + path, params=params).json().get('crew')

 
    cast_list = {}
    cast_list1 = []
    cast_list2 = []


    for i in range(len(response1)):
        if response1[i].get('cast_id') < 10:
            cast_list1.append(response1[i].get('name'))

   
    for j in range(len(response2)):
        if 'Directing' in response2[j].get('department'):
            cast_list2.append(response2[j].get('name'))
   
        cast_list = {"cast":cast_list1, "crew":cast_list2} 
                                                           
    
    return cast_list

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
