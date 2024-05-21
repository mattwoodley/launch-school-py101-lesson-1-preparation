# Write a function that takes one argument, a positive integer, and returns a string of alternating '1's and '0's, always starting with a '1'. The length of the string should match the given integer.

def stringy(integer):
    result = ""
    binary_bool = True

    while len(result) < integer:
        if binary_bool:
            result += "1"
            binary_bool = False
        else:
            result += "0"
            binary_bool = True

    return result


print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True
