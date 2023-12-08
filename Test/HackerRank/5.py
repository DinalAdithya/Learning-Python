students = []

for _ in range(int(input())):
    name = input()
    score = float(input())

    students.append([name, score])

print(students)
students.sort(key=lambda x: x[1])
print(students)

lowest_ss = students[0][1]
smf = [student for student in students if student[1] > lowest_ss]

print(smf)

lowest_score = smf[0][1]

lowest_students = [student[0] for student in smf if student[1] == lowest_score]
print(lowest_students)
lowest_students.sort()
print(lowest_students)
for name in lowest_students:
    print(name)
