# 프로젝트 02 - 파이썬 기반 데이터 활용

<br>

## 후기

다른 사람들에 비해 오래 걸린것같다.

열심히 한다고 했지만 부족한 부분이 많이 보이는것같다. json부분을 좀 더 복습해야할것같다. 아직도 코드를 짜는것에 대해서 능숙하지 못한 점이 많다. 하지만 조금씩 깨닫고있다는게 느껴진다. 더욱 정진하겠다.

<br>

## 풀이

[00.py]

``` python
import requests

order_currency = 'BTC'
payment_currency = 'KRW'
url = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'
response = requests.get(url).json()
coins = response.get('data')
print(coins.get('prev_closing_price'))
```

📌 손풀이용으로 출제된 문제, 수업시간에 배운걸 그대로 썼다. response.get으로 'data' 안의 전일 종가를 가져와서 출력했다.

coins뒤에 `.get('prev_closing_price')` 을  붙붙이고 coins를 출력해도 된다.

[01.py]

``` python
import requests
from pprint import pprint

# 9917f46b6425e1df8108a68c4d9202b0
def popular_count():
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': '9917f46b6425e1df8108a68c4d9202b0',
        'language': 'ko-KR',
    }

    response = requests.get(BASE_URL+path, params=params).json()
    cnt = 0
    for i in response.get('results'):
        cnt += 1

    return cnt


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
```

📌 여기서부턴 API를 잘 봐야한다. parameter에 어떤 값이 필수로 들어가는지, 경로는 무엇인지 확인을 하고 response.get으로 결과값을 출력하고 출력된 결과값 만큼 카운트해서 리턴하도록 했다.

[02.py]

``` python
import requests
from pprint import pprint


def vote_average_movies():
  BASE_URL = 'https://api.themoviedb.org/3'
  path = '/movie/popular'
  params = {
      'api_key': '9917f46b6425e1df8108a68c4d9202b0',
      'language': 'ko-KR'  
    }
  a = []
  response = requests.get(BASE_URL+path, params=params).json()
  for i in response['results']:
    if i['vote_average'] > 8:
      a.append(i)
  return a

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 반환
    (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(vote_average_movies())
```

📌 response에서 results의 값을 가져와 반복문으로 돌리면서 평균 평점이 8 이상인것만 리스트에 담아서 반환하도록 했다.

[03.py]

``` python

import requests
from pprint import pprint


def ranking():
  BASE_URL = 'https://api.themoviedb.org/3'
  path = '/movie/popular'
  params = {
      'api_key': '9917f46b6425e1df8108a68c4d9202b0',
      'language': 'ko-KR'  
    }
  response = requests.get(BASE_URL+path, params=params).json()
 
  result_list = []
  mov_list = []
  top_list = set()
  res = []

  for i in response['results']:
    mov_list.append(i)

  for j in range(len(response.get('results'))):   
    result = response.get('results')[j].get('vote_average') 
    result_list.append(result) 
    new = sorted(result_list,reverse= True) 
  
  for k in range(5):
    top_list.add(new[k])

     
  for h in top_list:
    for i in range(len(mov_list)):
      if mov_list[i]['vote_average'] == h:
        res.append(mov_list[i])
  return res

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화 반환
    (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(ranking())

```

📌 이 문제를 이런식으로 접근해서 푸는건지 잘 모르겠는데 앞전의 문제와 같이 results의 값을 반복문으로 돌려서 mov_list에 저장해놓는다. 그리고 result_list에는 평균 평점을 담아놓고 정렬을 한 후에 new에 담는다.

new에 담긴 평점들 중 상위의 5개 항목을 top_list에 넣고 중복을 제외한 값을 mov_list에 넣고, mov_list의 값이 top_list와 같은것들을 res에 담아서 넘긴다.

[04.py]

``` python
import requests
from pprint import pprint

# 검색
def search(title):
    movie_id = None
    BASE_URL='https://api.themoviedb.org/3'
    path='/search/movie'
    prams = {
            'api_key' : '9917f46b6425e1df8108a68c4d9202b0',
            'language': 'ko-KR', 
            'query': f'{title}' # 입력한 타이틀 값 검색
        } 
    response = requests.get(BASE_URL+path, params=prams).json()
    # 검색실패시
    if response == None: # 찾을 수 없는 값이 나올경우 None
        return None
    else:
        results = response.get('results') # 조회결과값 반환(리스트)
        for x in range(len(results)):
            movie_id = results[0].get('id') 
        return movie_id


def recommendation(title):
    movie_id = search(title) # 타이틀을 검색을 하면(title)값이 들어가 search로 보내짐
    if movie_id == None:
        return None
    BASE_URL='https://api.themoviedb.org/3'
    path=f'/movie/{movie_id}/recommendations'
    prams = {
            'api_key' : '9917f46b6425e1df8108a68c4d9202b0',
            'language': 'ko-KR'
        }
    
    response = requests.get(BASE_URL+path, params=prams).json()
    if response == None:
        return None
    else: 
        results = response.get('results')
        recommend_list = []
        for result in results:
            movie = result.get('title')
            recommend_list.append(movie)
        return recommend_list

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

```

📌 수업이 끝나고 강사선생님께 검색과 추천이 따로 만들어져야한다는 힌트를 듣고 뒤늦게 깨달았다. 이전의 것들만 생각하니까 이것도 전의 것처럼 해야지 라는 고정관념이 계속 넓은 생각을 방해하는것 같다.

recommendation()함수에 검색할 영화 제목을 넣으면, search로 넘어가 id값을 찾아내고  recommendation에 반환해서 추천 영화 제목을 가져오는 방식으로 만들었는데 3번째 케이스인 검색할 수 없는 영화에서 계속 None을 출력하지 못하고 오류가 생겼다. `UnboundLocalError: local variable 'movie_id' referenced before assignment` 오류였는데 movie_id가 선언되기 전에 참조되었다는 내용을 보고 이것저것 검색해서 알아보다가 search쪽에 movie_id의 초기값을 None으로 넣어주는걸로 해결이 됐다.

[05.py]

``` python
import requests
from pprint import pprint
# 9917f46b6425e1df8108a68c4d9202b0

def credits(title):
    movie_id = search(title)
    if movie_id == None:
        return None
    BASE_URL='https://api.themoviedb.org/3'
    path= f'/movie/{movie_id}/credits'
    prams = {
            'api_key' : '9917f46b6425e1df8108a68c4d9202b0',
            'language': 'ko-KR'
        }  
    response = requests.get(BASE_URL+path, params=prams).json()  
    if response == None:
        return None
    else:
        casts = response.get('cast')
        crews = response.get('crew')
        movie_dict = {"cast":[], "crew":[]}
        for cast in casts:
            if cast.get('cast_id') < 10: # 캐스트 id가 10 미만
                movie_dict['cast'].append((cast.get('name'))) # cast에 이름추가
        for crew in crews:
            if crew.get('department') == "Directing": # 부서가 Directing
                movie_dict['crew'].append((crew.get('name'))) # crew에 이름추가
        return movie_dict   


def search(title):
    movie_id = None
    BASE_URL='https://api.themoviedb.org/3'
    path='/search/movie'
    prams = {
            'api_key' : '9917f46b6425e1df8108a68c4d9202b0',
            'language': 'ko-KR', 
            'query': f'{title}' # 입력한 타이틀 값 검색
        } 
    response = requests.get(BASE_URL+path, params=prams).json()
    # 검색실패시
    if response == None: # 찾을 수 없는 값이 나올경우 None
        return None
    else:
        results = response.get('results') # 조회결과값 반환(리스트)
        for x in range(len(results)):
            movie_id = results[0].get('id') 
        return movie_id


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

```

📌 앞선 4번과 구현 방법은 비슷한데 dictionary에 cast와 crew값을 넣어서 반환하는게 달랐을 뿐인것같다. 조건은 과제에서 나온대로 캐스트 id가 10 미만, crew는 부서가 Directing인것만 담아서 반환했다.