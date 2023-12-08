file = open("gg.txt", "w")
file.write("text here")
file.close()


# 2nd way
with open("gg2", "w") as file2:
    file2.write("text here")
