from itertools import combinations, combinations_with_replacement

a = [1, 2, 3, 4]
comb = combinations(a, 2)  # length is mondatory here
print(list(comb))

# this will combine the number with itself
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))
