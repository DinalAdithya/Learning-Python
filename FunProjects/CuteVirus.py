from itertools import count
import os

for i in count():
    directory = "바보"+str(i)
    path = os.path.join(directory)
    os.mkdir(path)

#to stop at 10 uncomment below comments
#    if i == 10:
#        break




