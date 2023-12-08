num1 = float(input("Enter first value :"))
op   = str(input("Enter operator :"))
num2 = float(input("Enter secod value :"))

if op == "+" :
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/" :
    print(num1 / num2)
else:
    print("invalid operator")
