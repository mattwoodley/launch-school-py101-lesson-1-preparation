# Write a function that takes a year as input and returns the century. The return value should be a string that begins with the century number, and ends with 'st', 'nd', 'rd', or 'th' as appropriate for that number.

# New centuries begin in years that end with 01. So, the years 1901 - 2000 comprise the 20th century.


def century(year):
    century = 0
    current_year = year

    while current_year > 0:
        century += 1
        current_year -= 100

    if str(century).endswith('11') or str(century).endswith('12') or str(century).endswith('13'):
        return f'{century}th'
    elif str(century).endswith('1'):
        return f'{century}st'
    elif str(century).endswith('2'):
        return f'{century}nd'
    elif str(century).endswith('3'):
        return f'{century}rd'
    else:
        return f'{century}th'


print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True
