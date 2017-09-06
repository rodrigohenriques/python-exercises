# https://www.hackerrank.com/challenges/nested-list/problem

students = [[raw_input(), float(raw_input())] for _ in range(int(raw_input()))]
grades = list(set(map(lambda student: student[1], students)))
grades.sort()
secondSmallestGrade = grades[1]
studentsWithSecondSmallestGrade = filter(lambda s: s[1] == secondSmallestGrade, students)
studentsWithSecondSmallestGrade.sort()

for student in studentsWithSecondSmallestGrade:
    print student[0]
