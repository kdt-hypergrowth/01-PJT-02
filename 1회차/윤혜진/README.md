# 프로젝트 02 - 파이썬 기반 데이터 활용


## ▶ API란?
클라이언트에서 주소(URL)로 요청(request)을 보내면, 서버에서 문서(JSON 등)으로 응답(response)를 주는 시스템


## 🎯 목표
- Python 기본 문법(조건문, 반복문) 활용
- Python 외부 라이브러리(requests) 활용
- API([TMDB API](https://developers.themoviedb.org/3/getting-started/introduction)) 및 JSON 데이터의 활용


## 📢 프로젝트 안내
00. API 문서와 requests 활용 (연습)
    - 문제: [bithumb API 문서](https://apidocs.bithumb.com/reference/%ED%98%84%EC%9E%AC%EA%B0%80-%EC%A0%95%EB%B3%B4-%EC%A1%B0%ED%9A%8C)를 활용하여 BTC(비트코인)의 KRW(원) 전일종가를 출력하시오. 
    - 접근방법: requests 모듈을 이용해 해당 url에 대한 json 문서를 받은 후, 일부 정보만 가져와 반환.

01. 인기 영화 조회
    - 문제: TMDB에서 현재 인기 있는 영화 목록(Get Populations)을 가져와 1 페이지에서의 영화 갯수를 반환하는 함수를 작성하시오.
    - 접근방법: requests 모듈을 이용해 movies > Get Popular란에 명시되어 있는 url로 요청을 보내서 현재 인기 있는 영화 목록 데이터를 받음. len()함수로 영화 정보를 담은 요소의 갯수를 구해서 반환.

02. 특정 조건에 맞는 인기 영화 조회 1
    - 문제: TMDB에서 현재 인기 있는 영화 목록(Get Populations)을 가져온 후, 평점(vote_average)이 8점 이상인 영화 목록을 리스트로 반환하는 함수를 작성하시오.
    - 접근방법: requests 모듈을 이용해 movies > Get Popular란에 명시되어 있는 url로 요청을 보내서 현재 인기 있는 영화 목록 데이터를 받음. for 반복문을 돌면서 vote_average 키에 해당하는 값을 가져와 8 이상이면 리스트에 추가.

03. 특정 조건에 맞는 인기 영화 조회 2
    - 문제: TMDB에서 현재 인기 있는 영화 목록(Get Populations)을 가져온 후, 평점(vote_average)이 높은 영화 5개의 정보를 리스트로 반환하는 함수를 작성하시오.
    - 접근방법: requests 모듈을 이용해 movies > Get Popular란에 명시되어 있는 url로 요청을 보내서 현재 인기 있는 영화 목록 데이터를 받음. vote_average 키에 해당하는 값을 기준으로 sorted() 내림차순 정렬. sorted()함수는 리스트 데이터 타입으로 값을 반환하므로 인덱스 0부터 4까지의 데이터만 슬라이싱으로 가져와서 반환.

04. 영화 조회 및 추천 영화 조회
    - 문제: TMDB에서 영화제목으로 영화를 검색(Search Movies)한 결과를 가져온 후, 그중 첫번째 영화의 id 값을 활용하여 TMDB에서 추천 영화 목록(Get Recommendations)을 받아 리스트로 반환하는 함수를 작성.
    - 접근방법: requests 모듈을 이용해 search > Get Search Movies란에 명시되어 있는 url로 요청을 보내서 영화제목으로 영화를 검색한 결과 데이터를 받음 (이때 params 딕셔너리에 검색하고자하는 영화 제목을 추가해줘야 함). 결과 데이터에서 첫번째 영화의 id 값을 가져옴. 또 한번 requests 모듈을 이용해 movies > Get Popular란에 명시되어 있는 url로 요청을 보내서 이전에 받아온 영화 id와 연관된 추천 영화 목록 데이터를 받음. 추천 영화 목록의 title 값만 리스트에 담아 반환.

05. 출연진 및 연출진 데이터 조회
    - 문제: TMDB에서 영화제목으로 영화를 검색(Search Movies)한 결과를 가져온 후, 그중 첫번째 영화의 id 값을 활용하여 TMDB에서 해당 영화에 대한 출연진과 스태프 목록(Get Credits)을 받아, 출연진 중 cast_id 값이 10 미만인 출연진과 연출진 중 부서(department)가 Directing 인 연출진만 추출해, cast 와 directing 으로 구성된 딕셔너리에 추출된 값을 리스트로 출력하는 함수를 작성 
    - 접근방법: requests 모듈을 이용해 search > Get Search Movies란에 명시되어 있는 url로 요청을 보내서 영화제목으로 영화를 검색한 결과 데이터를 받음 (이때 params 딕셔너리에 검색하고자하는 영화 제목을 추가해줘야 함). 결과 데이터에서 첫번째 영화의 id 값을 가져옴. 또 한번 requests 모듈을 이용해 movies > Get Credits란에 명시되어 있는 url로 요청을 보내서 이전에 받아온 영화 id에서의 cast(출연진)/crew(연출진) 정보를 받아옴. 각각 특정 조건에 해당하는 cast/crew 데이터만 가져와 딕셔너리에 리스트 형식으로 값 추가.



## 🔔 추가 안내
- API key를 GitHub에 노출시키지 않으면서 로컬에서 활용하기 위해서는 프로젝트에서 환경 변수 파일을 `.env`로 관리하고, 이를 `.gitignore`에 추가함으로써 해결할 수 있음.
  - 파이썬에서는 주로 [python-dotenv](https://github.com/theskumar/python-dotenv)패키지를 설치해 환경 변수 설정 가능.


## 🗨 후기
오늘 처음 API라는 것을 이용해서 데이터에 접근 및 활용해봤다. 내가 평소에 사용했던 웹 사이트들이 이런 방식으로 정보를 주고 받는다는 사실을 알게 되니 정말로 신기했다. 마법이라 여겼던 현상이 이제는 이해가능한 영역이 된 것 같다. 오늘 프로젝트에서 사용한 TMDB API외에도 다양한 API를 사용해보며 더 공부해보고 싶다. 모호했던 개념인 API를 조금이나마 파헤쳐본 오늘이었다. 