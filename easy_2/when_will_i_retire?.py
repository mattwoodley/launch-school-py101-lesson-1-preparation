# Build a program that displays when the user will retire and how many years she has to work till retirement.

from datetime import datetime

current_age = int(input('What is your age? '))
retirement_age = int(input('At what age would you like to retire? '))
current_year = datetime.now().year
years_till_retirement = retirement_age - current_age
retirement_year = current_year + years_till_retirement

print(f"It's {current_year}. You will retire in {retirement_year}.")
print(f"You have only {years_till_retirement} years of work to go!")

"""
What is your age? 30
At what age would you like to retire? 70

It's 2024. You will retire in 2064.
You have only 40 years of work to go!
"""
