# 1을 한 번, 2를 두 번, 3을 세 번, 이런 식으로 1 2 2 3 3 3 4 4 4 4 5 .. 이러한 수열을 만들고 어느 일정한 구간을 주면 그 구간의 합을 구하는 것이다.
# 구현

A, B = map(int,input().split())
nums = []
result = []
for i in range(1,B+1):
    num = str(i)*i
    for j in num:
        nums.append(int(j))
print(sum(nums[A-1:B]))