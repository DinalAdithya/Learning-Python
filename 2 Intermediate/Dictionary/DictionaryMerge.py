my_dict = {"name": "max", "age": 28, "email": "gg@gmail.com"}
my_dict2 = dict(name="Marry", age=27, city="Boston")

my_dict.update(my_dict2)
print(my_dict)

# adding a Tuple in to a dictionary
my_tuple = ("ffff", 7)
my_dict = {my_tuple: 15}

print(my_dict)
