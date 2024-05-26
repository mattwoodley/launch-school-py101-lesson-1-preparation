# Write a function that takes two arguments, a string and a positive integer, then prints the string as many times as the integer indicates.


def repeat(word, number):
    while number > 0:
        print(word)
        number -= 1


repeat('Hello', 3)
