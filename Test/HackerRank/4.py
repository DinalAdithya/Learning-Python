n = int(input())
arr = map(int, input().split())

arr = list(arr)
uniq = list(set(arr))
print(uniq)
new_arr = list(uniq)
print(new_arr)
new_arr.sort(reverse=True)
print(new_arr)