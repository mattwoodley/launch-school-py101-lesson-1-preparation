# Write a function that returns a list that contains every other element of a list that is passed in as an argument. The values in the returned list should be those values that are in the 1st, 3rd, 5th, and so on elements of the argument list.
"""
def oddities(lst):
    index = 0
    odd_list = []
    while index < len(lst):
        odd_list.append(lst[index])
        index += 2
    return odd_list
"""

# Bonus question: Try to solve the problem using list slicing.


def oddities(lst):
    return lst[::2]


print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True


# Write a companion function that returns the 2nd, 4th, 6th, and so on elements of a list.

# Try to solve this differently from the exercise described above.

def evens(lst):
    return lst[1::2]


print(evens([2, 3, 4, 5, 6]) == [3, 5])     # True
print(evens([1, 2, 3, 4]) == [2, 4])        # True
print(evens(["abc", "def"]) == ['def'])     # True
print(evens([123]) == [])                   # True
print(evens([]) == [])                      # True
