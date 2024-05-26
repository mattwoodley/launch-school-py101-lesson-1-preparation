# Given a string that consists of some words and an assortment of non-alphabetic characters, write a function that returns that string with all of the non-alphabetic characters replaced by spaces. If one or more non-alphabetic characters occur in a row, you should only have one space in the result (i.e., the result string should never have consecutive spaces).

def clean_up(string):
    clean_string = ""

    for index in range(len(string)):
        if index == len(string) - 1:
            clean_string += string[index] if string[index].isalpha() else " "
            break

        if not string[index].isalpha() and not string[index + 1].isalpha():
            continue

        clean_string += string[index] if string[index].isalpha() else " "

    return clean_string


print(clean_up("---what's my +*& line?") == " what s my line ")  # True
