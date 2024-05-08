# Write a function that takes one integer argument and returns True when the number's absolute value is odd, False otherwise.

# input: integer
# output: boolean

# absolute value with abs() function

def abs_value_odd(number):
    return True if abs(number) % 2 == 0 else False


print(abs_value_odd(0))             # True
print(abs_value_odd(1))             # False
print(abs_value_odd(2))             # True
print(abs_value_odd(5))             # False
print(abs_value_odd(10))            # True
print(abs_value_odd(10000000001))   # False
print(abs_value_odd(-1))            # False
print(abs_value_odd(-241.44242))    # False
