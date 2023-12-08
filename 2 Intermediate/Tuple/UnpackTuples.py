my_tuple = "max", 24, "boston"

# this element names count need to be the same as element in tuple
name, age, city = my_tuple

print(name)
print(age, "\n")

# by adding a * here all the items in middle going to be a list
my_tuple2 = (1, 2, 3, 4, 5)
x1, *x2, x3 = my_tuple2

print(x1)
print(x2)
print(x3, "\n")

