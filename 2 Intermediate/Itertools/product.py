from itertools import product
a = [1, 2]
b = [3, 4]

prod = product(a, b)
print(list(prod), "\n") # printing it as a list, so we can see the details


# we can repeat the elements
# double the normal out put we get
a = [1, 2]
b = [3]

prod = product(a, b, repeat=2)
print(list(prod))
