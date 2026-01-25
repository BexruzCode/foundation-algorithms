#! Programming Basics.
#! Date: 25.01.2026.
#! Author: Behruz Khaitov.


def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number


number = int(input("Enter a number: "))
result = fizz_buzz(number)
print(result)
