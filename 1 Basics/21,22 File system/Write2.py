file = open("text.txt", "w")
try:
    file.write("Hellooow MFer")
finally: # no matter what happend in the end this is gonna run
    file.close()
