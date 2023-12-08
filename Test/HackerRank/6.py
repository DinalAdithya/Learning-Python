n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

element_total = 0

if query_name in student_marks:
    #print(f"marks of'{query_name}' :")
    n = 0
    for element in student_marks[query_name]:
        n += 1
        print(element)
        element_total += element

    avg_marks = element_total / n

    print("avreage marks : ", format(avg_marks, ".2f"))
