odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u, "\n")

# we get empty set because odds and evens don't have the same element
i = odds.intersection(evens)
print(i, "\n")

# this gives the same value(intersection)
x = odds.intersection(primes)
print(x, "\n")

# this will give number that are in both evens & primes
y = evens.intersection(primes)
print(y, "\n")


