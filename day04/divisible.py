#! Programming Basics.
#! Date: 23.01.2026.
#! Author: Behruz Khaitov.


def check_divisibility(number):
    if number % 5 == 0 and number % 10 == 0:
        return "Divisible by both 5 and 10."
    elif number % 5 == 0:
        return "Divisible by 5 only."
    else:
        return "Not divisible by 5 or 10."


number = int(input("Enter a number: "))
print(check_divisibility(number))
