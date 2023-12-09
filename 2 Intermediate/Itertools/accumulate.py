from itertools import accumulate
import operator

# sum
a = [1, 2, 3, 4]
acc = accumulate(a)

print("zigzag total")
print(a)
print(list(acc))

# multiplication
acc = accumulate(a, func=operator.mul)

print("\nzigzag multiplication")
print(a)
print(list(acc))

# max
a = [3, 2, 4, 1]
acc = accumulate(a, func=max)

print("\nzigzag maximum")
print(a)
print(list(acc))

