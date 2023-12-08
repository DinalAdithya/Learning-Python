from timeit import default_timer as timer

my_list = ["A"] * 16
print(my_list)

#2 methods to covert list to a string
# methode one
start = timer()

my_string = ''
for i in my_list:
    my_string += i
print(my_string)

stop = timer()
print(stop-start, "\n")


# method two (just remember 2nd method)
start = timer()

my_string = ''.join(my_list)
print(my_string)

stop = timer()
print(stop-start)

