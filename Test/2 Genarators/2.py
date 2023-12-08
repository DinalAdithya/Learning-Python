def topten():
    # return 5
    yield 5
    yield 9
    yield 2
    yield 3


values = topten()

"""print(next(values))"""
# next only need if I print one by one
# we normally do print with for loop, so we don't need next

for i in values:
    print(i)
