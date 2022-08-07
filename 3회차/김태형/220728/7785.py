# 상근이는 모든 사람의 출입카드 시스템의 로그를 가지고 있다. 이 로그는 어떤 사람이 회사에 들어왔는지, 나갔는지가 기록되어져 있다.
# 로그가 주어졌을 때, 현재 회사에 있는 모든 사람을 구하는 프로그램을 작성하시오.
# 해시

n = int(input())
dict = {}
for i in range(n):
    is_enter = input().split()
    dict[is_enter[0]]=is_enter[1]
for i in dict:
    if dict[i]=="enter":
        print(i)