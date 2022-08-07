# 태영이가 만들 수 있는 SASA 모형 개수의 최댓값을 구하라.

N, M = map(int,input().split())

if N>M:
    print(M//2)
else:
    print(N//2)