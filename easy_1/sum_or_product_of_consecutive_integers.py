# Write a program that asks the user to enter an integer greater than 0, then asks whether the user wants to determine the sum or the product of all numbers between 1 and the entered integer, inclusive.

# input
# int > 0

# output
# sum
# or
# product of all numbers between 1 and input (inclusive)

"""
def sum_of_range(limit):
    return sum(range(1, limit + 1))


def product_of_numbers(limit):
    total = 1
    for number in range(1, limit + 1):
        total *= number
    return total


while True:
    limit = input('Please enter a whole number greater than 0: ').strip()
    if not limit.isdigit():
        print('Invalid character.')
    elif int(limit) < 1:
        print('Number cannot be lower than 1.')
    else:
        limit = int(limit)
        break

while True:
    sum_or_product = input(
        'Enter "s" to compute the sum, or "p" to compute the product: ').strip()
    if sum_or_product.lower() == 's':
        total = sum_of_range(limit)
        print(
            f'The sum of the integers between 1 and {limit} is {total}.')
        break
    elif sum_or_product.lower() == 'p':
        total = product_of_numbers(limit)
        print(f'The product of the integers between 1 and {limit} is {total}.')
        break
    else:
        print('Only an "s" or "p" is valid.')
"""

# Further Exploration
# Suppose the input was a list of space separated integers instead of just a single integer? How would your compute_sum and compute_product functions change?

"""
# OLD ANSWER, CODE STILL VALID #
def product_of_numbers(numbers):
    outer_index = 0
    while outer_index < len(numbers):
        number = numbers[outer_index]
        counter = 1
        result = 1

        while counter <= number:
            result *= counter
            counter += 1

        outer_index += 1

        print(
            f'The product of the integers between 1 and {number} is {result:,}.')
"""

# Create empty dictionaries for all operations
sums = []
products = []

# This simply allows me to repeat the program endlessly for testing purposes
while True:

    # Accesses the max number of the user's input and compares it to the max key of the operation dictionary (sums or products). If the number is higher then call the appropriate function
    def compare_maximums(numbers, operation):
        max_number = numbers[-1]

        if sums:
            last_index = len(sums) - 1
        else:
            last_index = 0

        if operation == sums:
            if sums == []:
                create_sums(max_number)
            elif last_index < max_number and sums:
                update_sums(last_index, max_number)

        elif operation == products:
            create_products(max_number)

    def create_sums(max_number):
        counter = 0
        while counter <= max_number:
            sums.append(sum(range(1, counter + 1)))
            counter += 1

    def update_sums(last_index, max_number):
        while last_index < max_number:
            sums.append(sums[last_index] +
                        sums.index(sums[last_index]) + 1)
            last_index += 1

    def create_products(max_number):
        counter = 1
        result = 1
        while counter <= max_number:
            result *= counter
            products[counter] = result
            counter += 1

    # Loops through list of numbers using number as a key to print the value
    def print_operation(numbers, operation):
        for number in numbers:
            if operation == 's':
                print(
                    f'The sum of the integers between 1 and {number} is {sums[number]:,}.')
            elif operation == 'p':
                print(
                    f'The product of the integers between 1 and {number} is {products[number]:,}.')

    # Takes in a string input, converts to a list and validates into integers
    while True:
        user_input = input(
            'Please enter whole numbers greater than 0 that are separated by spaces: ').split(" ")

        user_numbers = sorted([int(number)
                               for number in user_input if number.isdigit() and int(number) > 0])

        if user_numbers:
            print(
                f'You have entered the following numbers: {user_numbers}')
            break
        else:
            print('Error: invalid input detected. Please try again.')

    # Takes in a string input and invokes the appropriate function
    while True:
        sum_or_product = input(
            'Enter "s" to compute the sum of these numbers, or "p" to compute the product: ').strip().lower()

        if sum_or_product == 's':
            compare_maximums(user_numbers, sums)
            print_operation(user_numbers, sum_or_product)
            break
        elif sum_or_product == 'p':
            compare_maximums(user_numbers, products)
            print_operation(user_numbers, sum_or_product)
            break
        else:
            print('Error: Only an "s" or "p" is valid.')

    print(sums)
