#new way since python  3.6
var = 3.123456
var2 = 6
new_string = f"the variable is {var} and {var2}"
print(new_string, "\n")

var = 3.123456
var2 = 6
new_string = f"the variable is {var:.2f} and {var2}"
print(new_string, "\n")

var = 3.123456
var2 = 6
new_string = f"the variable is {var*2} and {var2}"
print(new_string, "\n", "\n")

#old way
var = "place holder"
my_string = "This is a free space for %s" % var
print(my_string)

var = 1234
my_string = "This is a free space for %d" % var
print(my_string)

var = 10.23566
my_string = "This is a free space for %.2f" % var
print(my_string, "\n")

#old way part 2
var = 3.123456
var2 = 6
new_string = "the variable is {:.2f} and {}".format(var, var2)
print(new_string)
