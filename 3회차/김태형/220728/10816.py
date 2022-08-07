# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.
# 해시

N = int(input())
dict = {}
answer = []
n = list(map(int,input().split()))
for j in n:
    dict[j]=0
M = int(input())
m = list(map(int,input().split()))
for j in m:
    if j in dict:
        dict[j]+=1
for i in dict:
    print(dict[i],end=' ')