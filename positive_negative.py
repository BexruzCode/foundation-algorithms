#! Programming Fundamentals
#! Date: 06.01.2026
#! Author: Bexruz Khaitov

number = int(input("Enter a number: "))

def check_number(number):
    if number > 0:
        print("The number you entered is positive.")
    elif number == 0:
        print("The number you entered is zero.")
    else:
        print("The number you entered is negative.")

check_number(number)
