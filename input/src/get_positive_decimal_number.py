#! /usr/bin/python
#
# pylint: disable=line-too-long,invalid-name
#
'''
# Exercise No.   Final Project 3
# File Name:     get_positive_decimal_number.py
# Programmer:    Gary Powell
# Date:          Feb. 18, 2025
#
# Problem Statement: convert a string to an int or decimal
#   Check for bad inputs.
#
#
# Overall Plan:
'''
# import the necessary python libraries
from decimal import Decimal

def get_positive_decimal_number(response: str) -> Decimal:
    '''
    parse a string into either a decimal, or an int

    The calls to the conversion will throw an exception
    of ValueError if it fails to parse correctly.
    '''
    try:
        result: Decimal = Decimal(response)
    except Exception as exc:
        raise ValueError from exc

    if result < 0:
        raise ValueError
    return result

def main() -> None:
    '''
    Input a string, convert to a positive real number and print it.
    '''

    # Print a welcome message to the screen
    print("Welcome to the get a positive real number program.")

    input_text: str = input("Enter a positive real number: ")
    try:
        number: Decimal = get_positive_decimal_number(input_text)
        print(f"You entered {number}, which is a postive real number")
    except ValueError:
        print(f"{input_text} is not a positive real number")

    print("Done!")

# This code runs only when the module is executed directly.
if __name__ == '__main__':
    main()
