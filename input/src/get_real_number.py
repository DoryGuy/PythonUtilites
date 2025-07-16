#! /usr/bin/python
#
# pylint: disable=line-too-long,invalid-name
#
'''
# Exercise No.   MT Question 1
# File Name:     mtGetRealNumber.py
# Programmer:    Gary Powell
# Date:          Feb. 18, 2025
#
# Problem Statement: convert a string to an int or float
#   Check for bad inputs.
#
#
# Overall Plan:
'''
# import the necessary python libraries
from typing import Union

def get_real_number(response: str) -> Union[int, float]:
    '''
    parse a string into either a float, or an int

    The calls to the conversion will throw an exception
    of ValueError if it fails to parse correctly.
    '''
    is_possible_float: bool = False
    for char in response:
        if char in ('.', 'e'):
            is_possible_float = True
            break

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
        number: Union[int,float] = get_real_number(input_text)
        print(f"You entered {number}, which is a real number")
    except ValueError:
        print(f"{input_text} is not a real number")

    print("Done!")

# This code runs only when the module is executed directly.
if __name__ == '__main__':
    main()
