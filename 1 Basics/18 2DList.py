list_of_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(list_of_list[0][0])
print(list_of_list[1][0])

print("using for loops")

for row in list_of_list:
    for col in row:
        print(col)