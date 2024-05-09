# Write a program that asks for user's name, then greets the user. If the user appends a ! to their name, the computer will yell the greeting (print it using all uppercase).

name = input("What is your name? ")

print(
    f"Hello {name}." if not name.endswith("!") else
    f"HELLO {name.upper()} WHY ARE WE YELLING?")
