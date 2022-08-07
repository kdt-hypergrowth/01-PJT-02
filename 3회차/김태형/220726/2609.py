# 최대공약수와 최소공배수
# 정수론 # 유클리드 호제법

# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

# A와 B를 비교해 큰 수를 앞에 있도록 한다.
# 두 수를 나누어서 나머지가 0이면 작은 수가 최대공약수이다.
# 두 수를 나누어서 나머지가 0이면 큰 수가 최소공배수이다.

def gcd(a,b):
    if a<b:
        a,b=b,a
    if a%b==0:
        return a/b
    else:
        return gcd(b,a%b)

def lcm(a,b):
    if a<b:
        a,b=b,a
    m = gcd(a,b)
    if a%b==0:
        return a
    else:
        return m*(a/m*b/m)

A,B = map(int,input().split())
print(gcd(A,B))
print(lcm(A,B))