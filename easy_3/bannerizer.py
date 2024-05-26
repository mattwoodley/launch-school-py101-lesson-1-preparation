# Write a function that takes a short line of text and prints it within a box.

"""
def print_in_box(string):
    print(f'+-{"-" * len(string)}-+')
    print(f'| {" " * len(string)} |')
    print(f'| {string} |')
    print(f'| {" " * len(string)} |')
    print(f'+-{"-" * len(string)}-+')



print_in_box('To boldly go where no one has gone before.')

Output for Example 1

+--------------------------------------------+
|                                            |
| To boldly go where no one has gone before. |
|                                            |
+--------------------------------------------+

Example 1

print_in_box('')

Output for Example 2

+--+
|  |
|  |
|  |
+--+


print_in_box("")
print_in_box("To boldly go where no one has gone before.")
print_in_box("Is this going to work?")
"""


# Further Exploration

# Modify this function so that it truncates the message if it doesn't fit inside a maximum width provided as a second argument(the width is the width of the box itself). You may assume no maximum if the second argument is omitted.

"""
def print_in_box(string, max_length=None):
    if not max_length:
        length = len(string)
    else:
        length = max_length
        string = string[:max_length]

    print(f'+-{"-" * length}-+')
    print(f'| {" " * length} |')
    print(f'| {string} |')
    print(f'| {" " * length} |')
    print(f'+-{"-" * length}-+')


print_in_box("", 0)
print_in_box("To boldly go where no one has gone before.", 15)
print_in_box("Is this going to work?")
"""

# For a challenging but fun exercise, try word wrapping messages that are too long to fit, so that they appear on multiple lines but are still contained within the box. This isn't an easy problem, but it's doable with basic Python.

# CHARACTER WRAPPING

"""
def print_in_box(string, max_length=None):
    string_list = []
    if not max_length:
        length = len(string)
    else:
        length = max_length
        new_string = ""
        while len(string) > 0:
            new_string = string[:length]
            string_list.append(new_string)
            string = string[length:]

    print(f'+-{"-" * length}-+')
    print(f'| {" " * length} |')
    for string in string_list:
        print(f'| {string}{" " * (length - len(string))} |')
    print(f'| {" " * length} |')
    print(f'+-{"-" * length}-+')


print_in_box("", 0)
print_in_box("To boldly go where no one has gone before.", 10)
print_in_box("Is this going to work?", 13)
"""

# WORD WRAPPING


def print_in_box(string, length=None):
    if not length:
        max_length = len(string)
    else:
        max_length = length

    x = string.replace(" ", "* *")
    string_list = x.split('*')

    new_string = ""

    print(f'+-{"-" * max_length}-+')
    print(f'| {" " * max_length} |')

    for word in string_list:
        if len(new_string) + len(word) <= max_length:
            new_string += word
        else:
            print(f'| {new_string}{" " * (max_length - len(new_string))} |')
            new_string = word

    print(f'| {new_string}{" " * (max_length - len(new_string))} |')

    print(f'| {" " * max_length} |')
    print(f'+-{"-" * max_length}-+')


print_in_box("", 0)
print_in_box("To boldly go where no one has gone before.", 16)
print_in_box("Is this going to work?", 7)
