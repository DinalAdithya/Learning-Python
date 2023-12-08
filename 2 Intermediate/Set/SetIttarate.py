my_set = set()

my_set.add(1)
my_set.add(2)
my_set.add(3)
my_set.add(4)
my_set.add(5)
print(my_set, "\n")

for i in my_set:
    print(i)

#check weather number in my se or not
if 1 in my_set:
    print("yes")

if 2 in my_set:
    print("yes")

if 7 in my_set:
    print("yes")
else:
    print("no")

