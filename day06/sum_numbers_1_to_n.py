#! Programming Basics.
#! Date: 26.01.2026.
#! Author: Behruz Khaitov.


def sum_numbers(n):
    total = 0
    number = 1

    while number <= n:
        total += number
        number += 1

    return total


n = int(input("Enter N: "))
result = sum_numbers(n)
print(result)


