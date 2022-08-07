# 오르막길
# 구현

# 가장 큰 오르막길을 구하는 프로그램을 작성하시오.
# 오름차순이면 끝에서 처음을 뺀다.

N = int(input())
pi = input()
height = []
def slide(h):
    for i in range(len(h)):
        if h[i]>h[i-1]:
            top = h[i]
            height.append(top-h[0])

