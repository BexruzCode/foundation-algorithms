def max_of_three_numbers(a, b, c):
    if a >= b and a > c:
        return a
    elif b > a and b >= c:
        return b
    else:
        return c


a = int(input("Enter number A: "))
b = int(input("Enter number B: "))
c = int(input("Enter number C: "))

result = max_of_three_numbers(a, b, c)
print(f"The largest number is -> {result}")

