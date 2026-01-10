def age_category_checker(age):
    if age < 0:
        return "Invalid age!"
    elif age <= 12:
        return "Child"
    elif age <= 17:
        return "Teenager"
    else:
        return "Adult"


age = int(input("Enter your age: "))
print(age_category_checker(age))

