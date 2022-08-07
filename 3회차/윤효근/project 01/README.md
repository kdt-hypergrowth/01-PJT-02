# 프로젝트 01 - 파이썬 기반 데이터 활용

## 후기

 00. 텍스트 데이터 출력 (연습)

- 아래의 내용을  `00.txt`에 기록하시오.

### 결과 예시

```
N회차 홍길동
Hello, Python!
1일차 파이썬 공부 중
2일차 파이썬 공부 중
3일차 파이썬 공부 중
4일차 파이썬 공부 중
5일차 파이썬 공부 중
```

## 코드

```python
f = open("c:\\\\Users\\\\runed\\\\Desktop\\\\01-PJT-01\\\\3회차\\\\윤효근\\\\00.txt",'w')
f.write("3회차 윤효근\\nHello, Python!\\n")
for i in range(1,6):
    f.write("%d일차 파이썬 공부 중\\n"%i)

f.close()
```

## 느낀점



## 01. 텍스트 데이터 입력 (연습)

- 과일 데이터 

  ```
  fruits.txt
  ```

  를 활용하여 총 과일의 갯수를 

  ```
  01.txt
  ```

    에 기록하시오.

  - 과일은 하나당 한 줄에 기록되어 있습니다.

### 결과 예시

```
394
```

## 코드

```python
f = open("data\\\\fruits.txt",'r')
tmp = f.readlines()
count =0
for item in tmp:
    count+=1
w = open("01.txt",'w')
w.write(str(count))
f.close()
```

## 느낀점



## 02. 텍스트 데이터 활용 - 특정 단어 추출

- 과일 데이터 

  ```
  fruits.txt
  ```

  를 활용하여 

  ```
  berry
  ```

  로 끝나는 과일의 갯수와 목록을 

  ```
  02.txt
  ```

    에 기록하시오.

  - 과일은 하나당 한 줄에 기록되어 있습니다.

### 결과 예시

```
18
Honeyberry
Blackberry
Gooseberry
Juniper berry
Cranberry
Salal berry
Goji berry
Salmonberry
Bilberry
Cloudberry
Huckleberry
Raspberry
Mulberry
Elderberry
Marionberry
Strawberry
Boysenberry
Blueberry
```

## 코드

```python
from collections import OrderedDict

f = open("data\\\\fruits.txt",'r')
w=open("02.txt",'w')
tmp = f.readlines()
my_set = set(tmp)# 중복제거 set
my_list = list(my_set)#다시 리스트 생성
result =[]
count =0
for word in my_list:
    print()
    if word.find("berry")>0:
        print(word)
        count+=1
        result.append(word)
    
w.write(str(count)+'\\n')
for item in result:
    w.write(item)
```

## 느낀점



## 03. 텍스트 데이터 활용 - 등장 횟수

- 과일 데이터 `fruits.txt`를 활용하여 과일의 이름과 등장 횟수를  `03.txt` 에 기록하시오.

### 결과 예시

```
Boysenberry 3
Blueberry 4
Avocado 1
Marionberry 3
Date 9
...
Melon 1
berryfake 1
```

## 코드

```python
from collections import Counter

f = open("data\\\\fruits.txt",'r')
w=open("03.txt",'w')
tmp = f.readlines()
cnt = Counter(tmp)
for i in cnt.items():
    w.write(f'{i[0]}{i[1]}'+'\\n')
```

## 느낀점



## 04. JSON 데이터 활용 - 영화 단일 정보

- 영화 데이터 

  ```
  movie.json
  ```

   을 활용하여 필요한 정보로만 구성된 딕셔너리를 출력하시오.

  - 코드는 선언된 함수 내에 작성하며, 결과 딕셔너리를 반환합니다.
  - JSON으로 가져온 데이터가 함수의 인자로 전달됩니다.

- `id`, `title`, `vote_average`, `overview, genre_ids`으로 구성된 결과를 만듭니다.

### 결과 예시

```json
{'genre_ids': [18, 80],
 'id': 278,
 'overview': '촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 '
             '그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 '
             '쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 '
             '세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 '
             '이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...',
 'poster_path': '/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg',
 'title': '쇼생크 탈출',
 'vote_average': 8.7}
```

## 코드

```python
import json
from pprint import pprint

def movie_info(movie):
    # 여기에 코드를 작성합니다.
    d={}
    for k,v in movie.items():
        if k == "id" or k == "title" or k == "vote_average" or k == "overview" or k == "genre_ids":
            d[k]=v

    return d

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))
```

## 느낀점



## 05. JSON 데이터 활용 - 영화 단일 정보 응용

- 영화 데이터 

  ```
  movie.json
  ```

   와 

  ```
  genres.json
  ```

   을  활용하여 필요한 정보로만 구성된 딕셔너리를 출력하시오.

  - 코드는 선언된 함수 내에 작성하며, 결과 딕셔너리를 반환합니다.
  - JSON으로 가져온 데이터가 함수의 인자로 전달됩니다.

- id, title, vote_average, overview, genre_names로 결과를 만듭니다.

  - genre_names는 키로, 각 장르 정보를 값으로 가집니다.
  - genre_ids를 장르 번호에 맞는 name 값으로 대체합니다.

### 결과 예시

```json
{'genre_names': ['Drama', 'Crime'],
 'id': 278,
 'overview': '촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 '
             '그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 '
             '쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 '
             '세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 '
             '이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...',
 'title': '쇼생크 탈출',
 'vote_average': 8.7}
```

## 코드

```python
import json
from pprint import pprint

def movie_info(movie, genres):
    pass
    d={}
    for k,v in movie.items():
        if k == "id" or k == "title" or k == "vote_average" or k == "overview" :
            d[k]=v
        if k == "genre_ids":
            n= v
            for k in genres:
                if k['id'] == n[0] :
                    v=k['name']
                elif k['id'] == n[1]:
                    v2 =k['name']
            d['genre_names'] = [v,v2]

    return d
    # 여기에 코드를 작성합니다.  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
```

## 느낀점



## 06. JSON 데이터 활용 - 영화 다중 정보 활용

- 영화 데이터 

  ```
  movies.json
  ```

   와 

  ```
  genres.json
  ```

   을  활용하여 필요한 정보로만 구성된 리스트를 출력하시오.

  - 코드는 선언된 함수 내에 작성하며, 결과 딕셔너리를 반환합니다.
  - JSON으로 가져온 데이터가 함수의 인자로 전달됩니다.

- 전체 영화 정보는 평점 높은 20개의 영화 데이터입니다.

  - 개별 영화 정보는 id, title, vote_average, overview, genre_names로 결과를 만듭니다.
    - genre_names는 키로, 각 장르 정보를 값으로 가집니다.
    - genre_ids를 장르 번호에 맞는 name 값으로 대체합니다.

**TIP. 이전 단계의 코드를 활용할 수 있습니다.**

### 결과 예시

```json
[{'genre_names': ['Drama', 'Crime'],
  'id': 278,
  'overview': '촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 '    
              '그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 '    
              '쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 '   
              '세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 '
              '이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...',
  'title': '쇼생크 탈출',
  'vote_average': 8.7},
 {'genre_names': ['Drama', 'Crime'],
  'id': 238,
  'overview': '시실리에서 이민온 뒤, 정치권까지 영향력을 미치는 거물로 자리잡은 돈 꼴레오네는 갖가지 고민을 호소하는 사람들의 '
              '문제를 해결해주며 대부라 불리운다. 한편 솔로소라는 인물은 꼴레오네가와 라이벌인 탓타리아 패밀리와 손잡고 새로운 '
              '마약 사업을 제안한다. 돈 꼴레오네가 마약 사업에 참여하지 않기로 하자, 돈 꼴레오네를 저격해 그는 중상을 입고 '
              '사경을 헤매게 된다. 그 뒤, 돈 꼴레오네의 아들 소니는 조직력을 총 동원해 다른 패밀리들과 피를 부르는 전쟁을 '
              '시작하는데... 가족의 사업과 상관없이 대학에 진학한 뒤 인텔리로 지내왔던 막내 아들 마이클은 아버지가 총격을 '
              '당한 뒤, 아버지를 구하기 위해 위험천만한 협상 자리에 나선다.',
  'title': '대부',
  'vote_average': 8.7},
 {'genre_names': ['Drama', 'History', 'War'],
  'id': 424,
  'overview': '2차 세계대전 당시 독일군이 점령한 폴란드. 시류에 맞춰 자신의 성공을 추구하는 기회주의자 쉰들러는 유태인이 '
              '경영하는 그릇 공장을 인수한다. 그는 공장을 인수하기 위해 나찌 당원이 되고 독일군에게 뇌물을 바치는 등 갖은 '
              '방법을 동원한다. 그러나 냉혹한 기회주의자였던 쉰들러는 유태인 회계사인 스턴과 친분을 맺으면서 냉혹한 유태인 '
              '학살에 대한 양심의 소리를 듣기 시작한다. 마침내 그는 강제 수용소로 끌려가 죽음을 맞게될 유태인들을 구해내기로 '
              '결심하고, 독일군 장교에게 빼내는 사람 숫자대로 뇌물을 주는 방법으로 유태인들을 구해내려는 계획을 세우는데...',
  'title': '쉰들러 리스트',
  'vote_average': 8.6},
...
```

## 코드

```python
import json
from pprint import pprint

def movie_info(movies, genres):
    pass

    result=[]
    for k in movies:
        d = {}
        if k["id"]:
            value = k['id']
            d['id']=value
        if k['title']:
            value = k['title']
            d['title']=value
        if k['vote_average']:
            value = k['vote_average']
            d['vote_average'] = value
        if k['overview']:
            value = k['overview']
            d['overview']=value
        if k ["genre_ids"]:
            n= k["genre_ids"]
            list=[]
            for k in genres:
                for i in n:
                    if k['id'] == i:
                        list.append(k['name'])

            d['genre_names'] = list
        result.append(d)
    return result
    # 여기에 코드를 작성합니다.  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
```

## 느낀점

