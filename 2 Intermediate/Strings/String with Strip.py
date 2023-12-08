my_string = "      hello world         "
print(my_string.strip(), "\n")

print(my_string.upper().strip())
print(my_string.lower().strip())
print(my_string.startswith("hello"))
print(my_string.strip().startswith("hello"))

print(my_string.strip().find('lo'))
print(my_string.strip().find('l'))
print(my_string.strip().find('o'))
print(my_string.strip().find('p'))

print(my_string.replace('world', 'universe'))

