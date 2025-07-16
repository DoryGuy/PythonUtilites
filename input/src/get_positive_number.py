#! /usr/bin/python
#
# pylint: disable=line-too-long,invalid-name
#
'''
# Exercise No.   Hw6 Project 1
# File Name:     hw6GetNumber.py
# Programmer:    Gary Powell
# Date:          Feb. 16, 2025
#
# Problem Statement: convert a string to a positive int or float, or complex
#   Check for bad inputs.
#
#
# Overall Plan:
'''
# import the necessary python libraries
from typing import Union

def get_positive_number(response: str) -> Union[int, float, complex]:
    '''
    parse a string into either a float, or an int

    The calls to the conversion will throw an exception
    of ValueError if it fails to parse correctly.
    '''
    is_possible_float: bool = False
    is_possible_complex: bool = False
    for char in response:
        if char == 'j':
            is_possible_complex = True
            break
        if char in ('.', 'e'):
            is_possible_float = True
            """ we can't break here because it still might be complex."""

    if is_possible_complex:
        # negative complex numbers make no sense in this context
        result = complex(response)
    elif is_possible_float:
        result = float(response)
        if result < 0:
            raise ValueError
    else:
        result = int(response)
        if result < 0:
            raise ValueError

    return result

def main() -> None:
    '''
    Input a string, convert to a real number and print it.
    '''

    # Print a welcome message to the screen
    print("Welcome to the get a positive number program.")

    input_text: str = input("Enter a positive number: ")
    try:
        number: Union[int, float, complex]  = get_positive_number(input_text)
        print(f"You entered {number}, which is a number")
    except ValueError:
        print(f"{input_text} is not a positive number")

    print("Done!")

# This code runs only when the module is executed directly.
if __name__ == '__main__':
    main()
