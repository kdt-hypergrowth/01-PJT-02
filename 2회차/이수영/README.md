# 프로젝트 02 - 파이썬 기반 데이터 활용

## 후기

 프로젝트 01을 진행했던 지난주 보다 파이썬을 많이 접해 본 후 프로젝트를 진행하여서 막혀도 저번주 보다 답답하지 않았습니다. 프로그래밍을 하는 첫 단추인 API를 잘 끼워야 지만 다음 단계로 착실하게 나아 갈 수 있을 거 같다는 생각이 실습중에 들었습니다. 오늘 프로젝트 뿐만 아니라 다른 사이트의 API도 관심있게 보구 활용도 효율적으로 어떻게 할 수 있을까 생각해보도록 하겠습니다. 아직 마지막에 알려주신 개인 API 키를 숢기는 방법은 읽어봐도 잘 모르겠습니다. 주말 간 한번 더 보도록 하겠습니다.



## 예제 0

``` python
import requests

order_currency = 'BTC'  # 필요한 코인 이름 하나일때는 이름을 전부일때는 'ALL'
payment_currency = 'KRW'
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'
# URL 불러오기
response = requests.get(URL).json()
# 리퀘스트를 제이슨 형식으로 리스폰스로 저장

print(response.get('data').get('prev_closing_price'))
# 리스폰스 데이터 안에 전일 종가 딕셔너리 가져와서 프린트
```

API 기본이 되는 URL과 requests들을 가지고 기본적인 정보를 가져오는 문제였습니다.



## 예제 1

```python
import requests
BASE_URL = 'https://api.themoviedb.org/3'   # 필요 URL 불러오기
path = '/movie/popular'                      # 필요한 정보의 불러오기

params = {
    'api_key': '',    # API 키 입력
    'language': 'ko-KR'
}

response = requests.get(BASE_URL+path, params = params).json()
def popular_count():
    movies = response.get('results')     # URL에서 가져온 리스폰스를 Movies 라는 리스트로 생성
    return len(movies)                   # 생성된 리스트 안에 movie 정보 딕셔너리의 객체의 개수
   
```

다음은 URL에서 정보를 가져온 후 json으로 변경 딕셔너리 정보 안의 reults를 리스트로 작성 리스트 안의 movie 정보 딕셔너리의 수를 세는 명령어를 통해 결과갑을 출력했습니다.

## 예제 2

```python
response = requests.get(BASE_URL+path, params = params).json()

def vote_average_movies():
  top = []                       # 8점이상의 영화가 들어갈 리스트 생성
  movies = response.get('results')
  for movie in movies:
    if movie['vote_average'] >= 8:  # 평점 8점 이상 조건 생성
      top.append(movie)            #리스트 안에 8점 이상인 영화 등록
  return top
    
```

위의 문제들과 동일하게 정보를 가져와서 평점 8점이상의 조건문을 활용하였습니다.

## 예제 3

```python
def ranking():
  top5 = [] # 상위 5개의 영화 가 들어갈 리스트 작성
  movies = response.get('results')
  sor_movies = sorted(movies, key = lambda x: x['vote_average'], reverse = True)
  # movies 안에 있는 영화 정보는 딕셔너리이기 때문에 딕셔너리 각각의 평점을 정렬
  # 해야 한다. 그러기 위해서는 람다함수를 사용하여 sorted 함수의 키를 정하고 실행
  # 한다. 마지막 리버스를 돌려서 높은 순서가 먼저 나오게 한다.
  top5 = sor_movies[:5] # 0, 1, 2 ,3 , 4 까지 순서대로 출력
  return top5
```

예제 3은 정렬 함수인 sorted 함수를 사용하였습니다.  movies 안에 있는 영화 정보는 딕셔너리들 이기때문에 딕셔너리 안의 각각의 평점을 정렬할 수 없기 때문에 람다함수를 사용하여 sorted 함수의 키를 정하고 실행한다 라는 생각으로 람다함수를 사용 하였지만, 정확한 개념이 맞는지 또 언제 람다함수를 사용해야하는지 아직 개념정리가 확실하지 않습니다. 더 찾아보도록 하겠습니다.

## 예제 4

```python
def recommendation(title):
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key':'',
        'language': 'ko-KR',
        'query': title
        }
    response = requests.get(BASE_URL+path, params = params).json()
    movies = response.get('results')
    if movies ==[]:
        result = 'none'
    else:
        first_id = movies[0]['id']
        path_2 = f'/movie/{first_id}/recommendations'
        params = {
            'api_key':'',
            'language': 'ko-KR'
            }
        response = requests.get(BASE_URL+path_2, params = params).json()
        movies = response.get('results')
        result = []
        for movie in movies:
            result.append(movie['title'])
        return result  

```

이번 문제 같은 경우는 URL을 두번 사용해서 문제를 해결 해야 했기 때문에 다른 문제들에 비해서 많은 시간을 들여서 풀어야 했습니다. 하지만 이 과정을 통해 조금 더 정확히 URL사용 개념을 알 수 있게 되었습니다.



## 예제 5

```python

def credits(title):
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key':'',
        'language': 'ko-KR',
        'query': title
        }
    response = requests.get(BASE_URL+path, params = params).json()
    movies = response.get('results')
    if movies ==[]:
        result = 'none'
    else:
        first_id = movies[0]['id']
        path_2 = f'/movie/{first_id}/credits'
        params = {
            'api_key':'',
            'language': 'ko-KR'
            }
        response = requests.get(BASE_URL+path_2, params = params).json()
        casts = response.get('cast')
        crews = response.get('crew')
        main = []
        for cast in casts:
            if cast['cast_id'] < 10:
                main.append(cast)
        Fame = []
        for act in main:
            Fame.append(act['name'])
        people = []
        for crew in crews:
            if crew['department'] == 'Directing':
                people.append(crew)
        emp = []
        for person in people:
            emp.append(person['name'])
        all = {'cast': Fame, 'crew': emp}
        return all
        
```

조건문이 많아지긴 하였지만 예제 4번과 푸는 방식이 동일하여 풀 수 있었습니다.

  # 