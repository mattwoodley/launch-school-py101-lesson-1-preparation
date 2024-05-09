# Write a program that prompts the user for two positive numbers (floating-point), then prints the results of the following operations on those two numbers: addition, subtraction, product, quotient, floor quotient, remainder, and power. Do not worry about validating the input.

import operator

float1 = float(input("==> Enter the first number: "))
float2 = float(input("==> Enter the second number: "))

operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '//': operator.floordiv,
    '%': operator.mod,
    '**': operator.pow
}

for symbol, operation in operations.items():
    print(
        f'{float1} {symbol} {float2} = {operation(float1, float2)}')
