mydict = {"name": "max", "age": 25, "city": "NYC"}
print(mydict, "\n")

for key in mydict:
    print(key)

print("\n")

for i in mydict.keys():
    print(i)

print("\n")

for values in mydict.values():
    print(values)

print("\n""print key & value both :")

for key, values in mydict.items():
    print(key, values)

mydict_copy = mydict.copy()
print("copied dictionary :", mydict_copy)
