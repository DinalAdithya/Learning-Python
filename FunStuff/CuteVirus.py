from itertools import count
import os

for i in count():
    directory = "바보"+str(i)
    path = os.path.join(directory)
    os.mkdir(path)

#    if i == 10:
#        break




