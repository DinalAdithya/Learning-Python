mytuples = ("max", 24, "boston")
print(mytuples)
print(type(mytuples), "\n")

mytuples2 = "max", 24, "boston"
print(mytuples2)
print(type(mytuples2), "\n")

mytuples3 = ("max")
print(mytuples3)
print(type(mytuples3), "\n")

mytuples4 = ("max", )
print(mytuples4)
print(type(mytuples4), "\n")

print(mytuples[0], "\n")

if "max" in mytuples:
    print("yes", "\n")

# to convert tuple to list
mylist = list(mytuples)
print(mylist)

