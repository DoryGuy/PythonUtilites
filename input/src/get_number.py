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
# Problem Statement: convert a string to an int or float, or complex
#   Check for bad inputs.
#
#
# Overall Plan:
'''
# import the necessary python libraries
from typing import Union

def get_number(response: str) -> Union[int, float, complex]:
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
            break

    if is_possible_complex:
        return complex(response)
    if is_possible_float:
        return float(response)
    return int(response)

def main() -> None:
    '''
    Input a string, convert to a real number and print it.
    '''

    # Print a welcome message to the screen
    print("Welcome to the get a real number program.")

    input_text: str = input("Enter a real number: ")
    try:
        number: Union[int, float, complex]  = get_number(input_text)
        print(f"You entered {number}, which is a number")
    except ValueError:
        print(f"{input_text} is not a number")

    print("Done!")

# This code runs only when the module is executed directly.
if __name__ == '__main__':
    main()
