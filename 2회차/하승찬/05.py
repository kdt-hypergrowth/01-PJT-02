import requests
from pprint import pprint


def credits(title):
    pass 
        
n = input()
#추천영화목록 /movie/{movie_id}/recommendations   
base_ulr ='https://api.themoviedb.org/3'
spath = '/search/movie'   
sparams = {
    'api_key' : '9c84ae21c51581335eb9aca74793ddb9',
    'language' : 'ko-KR',
    'query'    :  f'{n}'
}

sresponse =requests.get(base_ulr + spath,params=sparams)

data= sresponse.json().get('results')

id_num =data[0].get('id')




dpath = f'/movie/{id_num}/credits'
dprams ={
    'api_key' : '9c84ae21c51581335eb9aca74793ddb9',
    'language' : 'ko-KR',
    }

dresponse=requests.get(base_ulr + dpath,params=dprams)

data_d = dresponse.json()#get('cast') #crew


cast_r= []
crew_r= []


for cast_i in range(len(data_d.get('cast'))): #캐스트 인원중 cast id값이 10 미만인 경우 cast리스트에 추가
    if data_d.get('cast')[cast_i].get('cast_id') < 10:
        cast_r.append(data_d.get('cast')[cast_i].get('name'))

for cast_i in range(len(data_d.get('crew'))): #크루 인원중 cast id값이 10 미만인 경우 cast리스트에 추가
    if data_d.get('crew')[cast_i].get('department') == 'Directing':
        crew_r.append(data_d.get('crew')[cast_i].get('name'))


creaidt= {"cast:": cast_r ,"crew": crew_r}

pprint(creaidt)

# # 아래의 코드는 수정하지 않습니다.
# if __name__ == '__main__':
#     """
#     제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
#     영화 id 검색에 실패할 경우 None을 반환
#     """
#     pprint(credits('기생충'))
#     # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
#     pprint(credits('검색할 수 없는 영화'))
#     # None
