# ✏프로젝트 02 - 파이썬 기반 데이터 활용

## 👊🏻목표
- Python 기본 문법(조건문, 반복문) 활용
- Python 외부 라이브러리 활용
- API와 JSON 데이터의 활용

## 💻개발 도구
- Visual Studio Code
- Python 3.9
- TMDB API [https://developers.themoviedb.org/3/getting-started/introduction](https://developers.themoviedb.org/3/getting-started/introduction)

## 📃문제
### 00. API 문서와 requests 활용 (연습)
- 아래의 문서를 활용하여 BTC(비트코인)의 KRW(원) 전일종가를 출력하시오.
- [https://apidocs.bithumb.com/reference/현재가-정보-조회](https://apidocs.bithumb.com/reference/%ED%98%84%EC%9E%AC%EA%B0%80-%EC%A0%95%EB%B3%B4-%EC%A1%B0%ED%9A%8C)
### 01. 인기 영화 조회
- 인기 영화 목록의 개수를 출력합니다.
- requests 라이브러리를 활용하여 TMDB에서 현재 인기 있는 영화 목록(Get Populations) 데이터를 요청합니다.
- 응답 받은 데이터 영화 개수를 반환하는 함수를 작성합니다.
### 02. 특정 조건에 맞는 인기 영화 조회
- 인기 영화 목록 중 평점이 8점 이상인 영화 목록을 출력합니다.
- requests 라이브러리를 활용하여 TMDB에서 현재 인기 있는 영화 목록(Get Populations) 데이터를 요청합니다.
- 응답 받은 데이터 중 평점(`vote_average`)이 8점 이상인 영화 목록을 리스트로 반환하는 함수를 작성합니다.
### 03. 특정 조건에 맞는 인기 영화 조회
- 인기 영화 목록을 평점이 높은 순으로 5개의 정렬하여 영화 데이터 목록을 출력합니다.
- requests 라이브러리를 활용하여 TMDB에서 현재 인기 있는 영화 목록(Get Populations) 데이터를 요청합니다.
- 응답 받은 데이터 중 평점(`vote_average`)이 높은 영화 5개의 정보를 리스트로 반환하는 함수를 작성합니다.
**TIP. 정렬시 sorted 함수의 key를 활용합니다.**
### 04. 영화 조회 및 추천 영화 조회
- 영화 제목으로 검색을 하여 추천 영화 목록을 출력합니다.
- requests 라이브러리를 활용하여 TMDB에서 영화제목으로 영화를 검색(Search Movies)합니다.
- 응답 받은 결과 중 첫번째 영화의 id 값을 활용하여 TMDB에서 추천 영화 목록(Get Recommendations)을 가져옵니다.
- 추천 영화 목록을 리스트로 반환하는 함수를 작성합니다.
### 05. 출연진 및 연출진 데이터 조회
- 제공된 영화 제목을 검색하여 해당 영화의 출연진(`cast`) 그리고 스태프(`crew`) 중 연출진으로 구성된 목록만을 출력합니다.
- requests 라이브러리를 활용하여 TMDB에서 영화제목으로 영화를 검색(Search Movies)합니다.
- 응답 받은 결과 중 첫번째 영화의 id 값을 활용하여 TMDB에서 해당 영화에 대한 출연진과 스태프 목록(Get Credits)을 가져옵니다.
- 출연진 중 `cast_id` 값이 `10 미만`인 출연진만 추출하고, 연출진은 부서(`department`)가 `Directing` 인 데이터만 추출합니다.
- `cast` 와 `directing` 으로 구성된 딕셔너리에 추출된 값을 리스트로 출력하는 함수를 작성합니다.
## 💪🏻후기
- 직접 `request` 모듈을 이용해서 API로 간단한 영화 서비스를 구현해서 실질적인 프로그래밍을 한 것 같아 뿌듯했다.
- 딕셔너리 안에 딕셔너리, 또는 리스트 등이 있는 복잡한 데이터 형식을 이용할 때 딕셔너리의 구조를 직접 출력해보며 답을 맞춰갈 때 짜릿함이 있었다.
- 이런 형식의 기능들을 합쳐서 나중에 큰 프로젝트를 구현하여 사람들에게 유용한 서비스를 제공할 날이 기대된다.✨