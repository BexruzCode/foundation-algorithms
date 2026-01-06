# Programming Basics
# Date: 06.01.2026
# Author: Behruz Khaitov

number = int(input("Enter a number: "))


def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total


print(sum_of_digits(number))
