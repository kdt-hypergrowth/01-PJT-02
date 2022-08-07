# 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
# 구현

cro = ["c=","c-","dz=","d-","lj","nj","s=","z="]
word = input()
count_cro = 0
no_cro = set()

for i in cro:
    for j in range(len(word)):
        if i==word[j:j+2]:
            count_cro+=1
            word=word.replace(i,"")
count_cro+=len(word)
print(count_cro)