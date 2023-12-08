from collections import namedtuple

point = namedtuple('point', 'x, y')
pt = point(1, -4)

print(pt, "\n")
print(pt.x, pt.y)
