
my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)

import sys
print("this example is to see that list is bigger than tuple in size", "\n")
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes", "\n")


#
import timeit
print("this example is to see that list is getting lot more time than tuple", "\n")
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]"))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)"))
