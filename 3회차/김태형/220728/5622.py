# 할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.
# 구현

words = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
w = input()
t = 0
for i in w:
    if i in words[0:3]:
        t+=3
    if i in words[3:6]:
        t+=4
    if i in words[6:9]:
        t+=5
    if i in words[9:12]:
        t+=6
    if i in words[12:15]:
        t+=7
    if i in words[15:19]:
        t+=8
    if i in words[19:22]:
        t+=9
    if i in words[22:26]:
        t+=10
print(t)