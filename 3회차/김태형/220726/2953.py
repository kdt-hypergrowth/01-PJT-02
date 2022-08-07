# 각 참가자가 얻은 평가 점수가 주어졌을 때, 우승자와 그의 점수를 구하는 프로그램을 작성하시오.
# 구현

score_list = []
for i in range(5):
    score = map(int,input().split())
    score_sum = sum(score)
    score_list.append(score_sum)
    for j in range(len(score_list)):
        if score_list[j]>score_list[j-1]:
            max_score = score_list[j]
            print(j+1,max_score)

