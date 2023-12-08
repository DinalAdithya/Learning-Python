mylist = [0] * 4
print(mylist)

mylist2 = [1, 2, 3, 4]

combain_list = mylist + mylist2
print(combain_list)


print("exclude 5th index        :", combain_list[1:5])
print("starting from beginning  :", combain_list[:5])
print("from 2 index till the end:", combain_list[2:])
print("to reverse the list      :", combain_list[::-1])
print("every other index from 0 :", combain_list[0::2])
print("this call slicing        :", combain_list[:])
#slicing use to copy the list as well
#copy_list = combain_list
#this way is to make them the same not to copy
#copy_list = combain_list[:] # this way is to copy the original to new

