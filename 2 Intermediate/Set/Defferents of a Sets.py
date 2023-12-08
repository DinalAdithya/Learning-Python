setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

# this will rettern attribute that are in set A & not on B
deff = setA.difference(setB)
print(deff)

# other way returns the opposite
deff = setB.difference(setA)
print(deff)

#this will take all the unique values to both set A & B
diff = setB.symmetric_difference(setA)
print(diff)

'''#update setA values by adding what's not in that set
setA.update(setB)
print(setA)'''

'''# update setA by adding element that are in both sets
setA.intersection_update(setB)
print(setA)'''

'''#update the setA by removing what's on the setB
setA.difference_update(setB)
print(setA)'''

'''# update setA by removing element that are in both set & adding new element
setA.symmetric_difference_update(setB)
print(setA)'''
