setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}

print(setA.issubset(setB))
print(setA.issuperset(setB), "\n")

print(setB.issubset(setA))
print(setB.issuperset(setA), "\n")

# return true if they don't have same element
print(setA.isdisjoint(setB))

setC = {7, 8}

print(setA.isdisjoint(setC))
