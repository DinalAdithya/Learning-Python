setA = {1, 2, 3, 4, 5, 6}

# by doing this set does not copy but mirror
setB = setA

setB.add(7)

print(setA)
print(setB, "\n")

#this how just copy
setC = setA.copy()
setC.add(9)
print(setC, "\n")

#or this will also make a copy
setD = set(setA)
print(setD)

