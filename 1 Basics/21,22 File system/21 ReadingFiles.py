# file modes r , r+, w, a
# w = overwrite the whole fing file
# w = aslo can create new files
game_type = open("Games.txt", "r")

# to check weather file is readable or not
print(game_type.readable())

# to read whole file
##print(game_type.read())

'''
 this code going to read only one line but
 if the whole file already read this code not gonna print any-thing
'''
##print(game_type.readline())
'''
 if we didn't read the whole file then this code gonna read a line 
 that didn't read [next in line] & keep the finger on the 
 line after that.
 
 if we readline() again the its gonna start reading where the 
 finger is. basically next line
'''
##print(game_type.readline())

'''
 To read the text file as an array.
 
 even if we gave the array index to read the data if the 
 first data had been read before then in this file reading commands
 they are gonna consider what left, So even if I ask for 0th index 
 if it already read then they are gonna give me 1st index.
'''
##print(game_type.readlines()[0])

for game in game_type.readlines():
    print(game.strip())

# you must close what you open
game_type.close()
