# Write a function that takes a string argument and returns a new string that contains the value of the original string with all consecutive duplicate characters collapsed into a single character.

"""
def crunch(string):
    index = 0
    current_char = ''
    crunched_string = []

    while index < len(string):
        if index == len(string) - 1:
            crunched_string.append(string[index])
            break

        if string[index] == string[index + 1] and string[index] is not current_char:
            current_char = string[index]

        if string[index] != string[index + 1]:
            crunched_string.append(string[index])
            current_char = string[index + 1]
        index += 1

    return "".join(crunched_string)
"""


def crunch(string):
    index = 0
    crunched_string = ''

    while index < len(string):
        if index == len(string) - 1 or string[index] != string[index + 1]:
            crunched_string += string[index]
        index += 1
    return crunched_string


# Further Exploration

# Regular expressions are also available in Python through the re module. If you're familiar with regular expressions, you can try to solve this problem using that module. Additionally, can you think of any other solutions that don't involve regular expressions, perhaps using Python's built-in string or list methods?


print(crunch('ddaaiillyy ddoouubbllee'))
print(crunch('4444aabcabccba'))
print(crunch('ggggggggggggggg'))
print(crunch('abc'))
print(crunch('a'))
print(crunch(''))
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444aabcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')
