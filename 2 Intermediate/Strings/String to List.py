#defult splitting point is space
my_string = "how are you doing"
my_list = my_string.split()
print(my_list)


my_string = "how,are,you,doing"
my_list = my_string.split()
print(my_list)

my_string = "how,are,you,doing"
my_list = my_string.split(",")
print(my_list)

new_string = ' '.join(my_list)
print(new_string)
