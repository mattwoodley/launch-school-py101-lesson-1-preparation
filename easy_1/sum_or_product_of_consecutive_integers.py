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

# Create lists for all operations
sums = [0]
products = [0]

# while True keeps the program running once activated in the terminal
while True:

    # operation parameter checks which function to invoke
    # checks whether list has been operated on previously
    # if not then invoke create_operation(max_number)
    # if it has then check (max_number > last_index of list)
    # if True then update_operation(max_number)
    def create_or_update(operation, max_number):
        if operation == 's':
            if len(sums) == 1:
                create_sums(max_number)
            elif len(sums) > 1 and max_number > len(sums) - 1:
                update_sums(max_number)

        if operation == 'p':
            if len(products) == 1:
                create_products(max_number)
            elif len(products) > 1 and max_number > len(products) - 1:
                update_products(max_number)

    def create_sums(max_number):
        for number in range(1, max_number + 1):
            sums.append(sum(range(1, number + 1)))

    def update_sums(max_number):
        last_index = sums.index(sums[-1])
        for number in range(last_index, max_number):
            sums.append(sums[-1] +
                        sums.index(sums[-1]) + 1)

    def create_products(max_number):
        result = 1
        for number in range(1, max_number + 1):
            result *= number
            products.append(result)

    def update_products(max_number):
        last_index = products.index(products[-1])
        for number in range(last_index, max_number):
            products.append(products[-1] *
                            (products.index(products[-1]) + 1))

    def print_operation(numbers, operation):
        for number in numbers:
            if operation == 's':
                print(
                    f'The sum of the integers between 1 and {number} is {sums[number]:,}.')
            elif operation == 'p':
                print(
                    f'The product of the integers between 1 and {number} is {products[number]:,}.')

    # input a string, convert to list and validate into sorted integers
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

    # input a string to determine which function to invoke
    # create variable of largest number and pass into create_or_update()
    while True:
        sum_or_product = input(
            'Enter "s" to compute the sum of your numbers, or "p" to compute the product: ').strip().lower()
        max_number = user_numbers[-1]

        if sum_or_product == 's':
            create_or_update('s', max_number)
            print_operation(user_numbers, sum_or_product)
            break
        elif sum_or_product == 'p':
            create_or_update('p', max_number)
            print_operation(user_numbers, sum_or_product)
            break
        else:
            print('Error: Only an "s" or "p" is valid.')

    print(sums)
    print(products)
