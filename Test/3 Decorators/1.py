def subtract(a, b):
    print(a / b)


def swapper(fun):
    def inner(a, b):
        if a < b:
            a, b = b, a

        return fun(a, b)

    return inner


subtract = swapper(subtract)
# connect the 2 function [only in python :D]

subtract(2, 10)
