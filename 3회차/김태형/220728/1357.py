# 두 양의 정수 X와 Y가 주어졌을 때, Rev(Rev(X) + Rev(Y))를 구하는 프로그램을 작성하시오.
# 구현

X, Y = map(int,input().split())
X = int(str(X)[::-1])
Y = int(str(Y)[::-1])
sums = X+Y
rev_sum = int(str(sums)[::-1])
print(rev_sum)