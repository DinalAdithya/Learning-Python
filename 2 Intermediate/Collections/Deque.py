# double ended queue this will allow us to add or remove the element from both ends.
from collections import deque

d = deque()

d.append(1)
d.append(2)
print(d, "\n")

d.appendleft(3)
print(d, "\n")

d.pop()
print(d, "\n")

d.popleft()
print(d, "\n")

d.append(2)
d.append(3)
print(d, "\n")

d.clear()
print(d, "\n")

d.extend([4, 5, 6])
print(d, "\n")

d.extendleft([3, 2, 1])
print(d, "\n")

# all elements one place to the right
# in other words 6 becomes the first element, first element become second
d.rotate(1)
print(d)

# dose the opposite of that [ move places to left ]
d.rotate(-1)
print(d)

#move 2 places to the right
d.rotate(2)
print(d)
