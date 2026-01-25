#! Programming Basics.
#! Date: 25.01.2026.
#! Author: Behruz Khaitov.


def calculator(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "You cannot divide by zero"
        else:
            return num1 / num2
    else:
        return "Invalid operator"


num1 = int(input("Enter the first number: "))
operator = input("Choose an operator (+, -, *, /): ")
num2 = int(input("Enter the second number: "))

result = calculator(num1, operator, num2)
print(result)
