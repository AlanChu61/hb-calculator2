"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

# [operand,num1,num2]
while True:
    tokens = input("Enter your equation > ").split(" ")
    operand = tokens[0]
    try:
        num1 = int(tokens[1])
        num2 = int(tokens[2]) if len(tokens) == 3 else 0
    except ValueError:
        print("Input numbers not valid")
        continue
    if 'q' in tokens:
        print("Exit")
        break
    elif len(tokens) < 2:
        print("Not enough data to implement!")
        continue

    if operand == "+":
        result = add(num1, num2)
    elif operand == "-":
        result = subtract(num1, num2)
    elif operand == "*":
        result = multiply(num1, num2)
    elif operand == "/":
        result = divide(num1, num2)
    elif operand == "square":
        result = square(num1)
    elif operand == "cube":
        result = cube(num1)
    elif operand == "pow":
        result = power(num1, num2)
    elif operand == "mod":
        result = mod(num1, num2)
    else:
        print("Not valid operand")
        continue
    print(round(result, 1))
