#! Programming Basics.
#! Date: 23.01.2026.
#! Author: Behruz Khaitov.


def grade(score):
    if score == 1:
        return "Very bad"
    elif score == 2:
        return "Unsatisfactory"
    elif score == 3:
        return "Satisfactory"
    elif score == 4:
        return "Good"
    elif score == 5:
        return "Excellent"
    else:
        return "Invalid grade"


score = int(input("Enter the grade (1-5): "))
print(grade(score))

