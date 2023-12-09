from itertools import count, cycle, repeat

#count
for i in count(2): # in here starting value is 2
    print(i)
    if i == 10:
        break

# cycle
a = [1, 2, 3]
for i in cycle(a): # this will return the element of the list 'a' over and over
    print(i)

# repeat
a = [1, 2, 3]
for i in repeat(a, 4): # this will print the entire list over and over
    print(i)

