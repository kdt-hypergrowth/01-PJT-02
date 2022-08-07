# sorted() 내장함수

student_tuples = [ ('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
aged_student = sorted(student_tuples, key=lambda student: student[2])   # student_tuples의 인덱스 [2]를 이용하여 정렬 --- sort by age 

print(aged_student)
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)] -- sorted의 기본값은 오름차순 정렬