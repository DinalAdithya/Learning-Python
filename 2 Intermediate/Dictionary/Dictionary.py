mydict = {"name": "max", "age": 25, "city": "NYC"}
print(mydict)

# to add a new recode
mydict["email"] = "max@gmail.com"
print(mydict)
# by doing it again its overwritten
mydict["email"] = "coolmax@gmail.com"
print(mydict)

# to remove a key
del mydict["name"]
print(mydict)
# second method
mydict.pop("age")
print(mydict)
# Thread method (in this way it removes the last element
mydict.popitem()
print(mydict)

#cheking the key is there or not from 2 methods
print("\n""Checking the city in the dictionary or not")
if "city" in mydict:
    print("yes", "\n")

print("Checking the last name on the dictionary or not")
try:
    print(mydict["lastname"])
except:
    print("Error")
