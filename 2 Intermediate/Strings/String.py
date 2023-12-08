# string are immutable can not change
my_string = """hello 
world"""
print(my_string, "\n")


my_string = """hello \
world"""
print(my_string, "\n")


my_string = "hello world"
char = my_string[0]
print(char, "\n")

my_string = "hello world"
char = my_string[-1]
print(char, "\n")

my_string = "hello world"
char = my_string[::2]
print(char, "\n")

my_string = "hello world"
char = my_string[::-1]
print(char, "\n")

