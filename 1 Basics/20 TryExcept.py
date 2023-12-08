try:
    #n = 10/0
    number = int(input("Enter Number :"))
    print(number)

#err type 1 if divided by 0
except ZeroDivisionError as err:
    print(err)

#err 2 = if input is not  integer
except ValueError:
    print("That's not a number u idiot")
