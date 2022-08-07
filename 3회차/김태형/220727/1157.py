# 단어 공부
# 구현

# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

word = input().upper()
alphabet = list(set(word))
count_list = []
for i in range(len(alphabet)):
    if word.count(alphabet[i])>word.count(alphabet[i-1]):
        result = alphabet[i]
    elif word.count(alphabet[i])<word.count(alphabet[i-1]):
        result = alphabet[i-1]
    else:
        result = "?"
print(result)