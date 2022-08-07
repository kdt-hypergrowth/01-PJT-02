# 분해합
# 부르트포스 방법론

# 자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.
# 생성자 : 자신과 각 자리수를 더해서 N이 되는 가장 작은 수
# N : a+a[0]+a[1]+...

N = int(input())
for i in range(N):
    num=str(i)
    num_sum=0
    for j in num:
        num_sum+=int(j)
    if N==int(num)+num_sum:
        print(num)
