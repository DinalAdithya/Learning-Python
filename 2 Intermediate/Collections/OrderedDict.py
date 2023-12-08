# what OrderedDict dose is it remember the items ware inserted.
# this is less important now because after Python 3.7 normal dict also dose the same

from collections import OrderedDict

ordered_dict = OrderedDict()

ordered_dict["d"] = 2
ordered_dict["c"] = 4
ordered_dict["a"] = 3
ordered_dict["a"] = 1

print(ordered_dict)

# normal dict
# just to see both dose the same thing now and normal dict using fewer raw's

my_dict = {}

my_dict["d"] = 2
my_dict["c"] = 4
my_dict["a"] = 3
my_dict["a"] = 1

print(my_dict)
