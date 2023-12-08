is_male = True
is_tall = True

if is_male and is_tall:
    print("you are tall male")

elif is_male and not(is_tall):
    print("you are short male")

elif not(is_male) and is_tall:
    print("you are not a male but tall")

else:
    print("you are not a male or tall")

