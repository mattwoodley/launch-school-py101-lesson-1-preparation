# Using the multiply function from the "Multiplying Two Numbers" exercise, write a function that computes the square of its argument (the square is the result of multiplying a number by itself).

def multiply(num1, num2):
    return num1 * num2


def square(num):
    return multiply(num, num)


print(square(5) == 25)   # True
print(square(-8) == 64)  # True

# Suppose we want to generalize this function to a "power to the n" type function: cubed, to the 4th power, to the 5th, etc. How would we go about doing so while still using the multiply function?


def power_of(num, power):
    result = multiply(num, num)
    for number in range(1, power):
        result = multiply(result, num)
    return result


print(power_of(2, 3))
print(power_of(2, 6))
print(power_of(2, 6) == 128)
