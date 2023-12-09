# all possible ordering of input

from itertools import permutations

a = [1, 2, 3]
perm = permutations(a)
print(list(perm), "\n")# printing it as a list, so we can see the output

# ordering according to the length
a = [1, 2, 3]
perm = permutations(a, 2)# specify the length here
print(list(perm))

