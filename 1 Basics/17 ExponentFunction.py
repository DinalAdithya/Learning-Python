def power(num1, num2):
    result = 1
    for i in range(num2):
        result = result * num1
    return result

print(power(3, 2))