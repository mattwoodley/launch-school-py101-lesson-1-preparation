# Build a program that asks the user to enter the length and width of a room, in meters, then prints the room's area in both square meters and square feet.

# Note: 1 square meter == 10.7639 square feet

"""
length = float(input('Please enter the length of the room in metres: '))
width = float(input('Please enter the width of the room in metres: '))

square_metres = length * width
square_feet = square_metres * 10.7639

print(f'{square_metres} square metres and {round(square_feet, 3)} square feet.')
"""

# Modify the program to let the user specify the measurement type (meters or feet). Compute the area accordingly and print it and its conversion in parentheses.

room_length = float(input('Please enter the length of the room in metres: '))
room_width = float(input('Please enter the width of the room in metres: '))
measurement_type = input('Would you like to measure in metres or feet? ')

match measurement_type.lower():
    case 'metre' | 'metres' | 'meter' | 'meters':
        print(
            f'The area of the room is {room_length * room_width:.2f} metres. ({room_length} * {room_width})')
    case 'feet' | 'feets':
        print(
            f'The area of the room is {(room_length * room_width) * 10.7639:.2f} feet. ({room_length} * {room_width} * 10.7639)')
    case _:
        print("I'm sorry, I didn't recognise which measurement you entered. Please enter either 'metres' or 'feet'.")
