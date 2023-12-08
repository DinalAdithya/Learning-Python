# if the value does not exist this will give us a default value
from collections import defaultdict

d = defaultdict(int) # if we need to get the output as float,list,tuple we can simply use it here
d['a'] = 1
d['d'] = 2

print(d['a'])
print(d['d'])
print("not existing value :", d['c'])

