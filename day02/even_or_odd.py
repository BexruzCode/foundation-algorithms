#! Programming Basics
#! Date: 07.01.2026
#! Author: Behruz Khaitov


def even_or_odd(number):
    if number % 2 == 0:
        return "Even number"
    return "Odd number"


number = int(input("Enter a number: "))
print(even_or_odd(number))
