# In the previous exercise, we assumed that the Gregorian calendar has been in continuous use since since the year 1. However, the Gregorian calendar wasn't adopted until much later
# prior to that, much of the world used the Julian calendar, which observed leap year every 4 years.

# in 1752, England, Ireland, and the British colonies all switched to the Gregorian calendar. Update the function from the previous exercise so it uses the Julian calendar prior to 1752, and the Gregorian calendar starting in 1752.

"""
def is_leap_year(year):
    if type(year) != int or year < 1:
        print("ValueError: Year must be an integer and cannot be less than 1.")
        return

    if year < 1752 and year % 4 == 0:
        return True
    elif year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return year % 4 == 0


# These examples should all print True
print(is_leap_year("whoops") == None)
print(is_leap_year(0) == None)
print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == True)
print(is_leap_year(1100) == True)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == True)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)
"""

# Further Exploration

# Different regions adopted the Gregorian calendar at different times. Investigate when it was adopted in various countries and how that transition was managed. Consider how this would impact the leap year calculation and potentially adjust the solution based on the country of reference.

# Some countries like Canada changed to the Gregorian calendar, only to then change to a different calendar and then later back to the Gregorian calendar. Other countries like Germany changed their calendar at different times depending on the region within the country.

# This all means that if our leap year program is to be accurate, then it would need to factor in not just the country but also any regions specific to that country.
