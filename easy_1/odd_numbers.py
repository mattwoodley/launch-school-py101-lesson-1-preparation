# Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.
# Bonus Question: Can you solve the problem by iterating over just the odd numbers?

"""
for number in range(1, 100, 2):
    print(number)
"""

# Consider adding a way for the user to specify the starting and ending values of the odd numbers printed.

print('Please enter the range of odd numbers (inclusive)')
starting_value = int(input('Enter the starting value: '))
end_value = int(input('Enter the end value: '))

for number in range(starting_value, end_value + 1):
    if number % 2 == 1:
        print(number)