# Start number from 1
number = 1

# Take input from the user
n = int(input("Enter N: "))


# Function to print numbers from 1 to N
def print_numbers(number):
    # Loop until number becomes greater than N
    while number <= n:
        # Print current number
        print(number)
        # Increase number by 1
        number += 1


# Call the function
print_numbers(number)

