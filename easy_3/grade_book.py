# Write a function that determines the mean (average) of the three scores passed to it, and returns the letter associated with that grade.

def get_grade(english, maths, science):
    score = (english + maths + science) / 3

    if 0 < score < 60:
        return 'F'
    elif 60 <= score < 70:
        return 'D'
    elif 70 <= score < 80:
        return 'C'
    elif 80 <= score < 90:
        return 'B'
    elif 90 <= score <= 100:
        return 'A'


print(get_grade(10, 20, 30) == "F")
print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True


"""
Numerical score letter grade list:



Tested values are all between 0 and 100. There is no need to check for negative values or values greater than 100.
"""
