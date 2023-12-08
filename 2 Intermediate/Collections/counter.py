#spashal container data types.

from collections import Counter
# counter store elements as key and there count as values
a = "AAAAABBBBCC"
my_counter = Counter(a)

print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())

print(my_counter.most_common(1))
print(my_counter.most_common(2))
print(my_counter.most_common())

#to get most comment elements
print(my_counter.most_common(1)[0][0])

# to get all the elements and print it as a list
print(list(my_counter.elements()))
