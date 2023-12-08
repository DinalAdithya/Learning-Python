N = int(input())
Alist = []
count = 1

for i in range(N):
    command = input().split()
    count += 1
    if command[0] == "insert":
        Alist.insert(int(command[1]), int(command[2]))
    elif command[0] == "append":
        Alist.append(int(command[1]))
    elif command[0] == "remove":
        Alist.remove(int(command[1]))
    elif command[0] == "sort":
        Alist.sort()
    elif command[0] == "pop":
        Alist.pop()
    elif command[0] == "reverse":
        Alist.reverse()
    elif command[0] == "print":
        print(Alist)

    if count == N:
        print(Alist)
        break


