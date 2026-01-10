#! Programming Basics
#! Date: 10.01.2026
#! Author: Behruz Khaitov


def max_of_three_numbers(a, b, c):
    if (b <= a) and (a > c):
        return a
    elif (a < b) and (b >= c):
        return b
    else:
        return c


a = int(input("Enter number A: "))
b = int(input("Enter number B: "))
c = int(input("Enter number C: "))

result = max_of_three_numbers(a, b, c)
print(f"The largest number is -> {result}")

