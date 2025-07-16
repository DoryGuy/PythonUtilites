#! /usr/bin/python
#
# pylint: disable=line-too-long,invalid-name
#
"""
# Exercise No.   Hw12 Project 1
# File Name:     get_positive_integer.py
# Programmer:    Gary Powell
# Date:          Feb. 20, 2025
#
# Problem Statement: convert a string to an int
#   Check for bad inputs.
#
#
# Overall Plan:
"""
# import the necessary python libraries

def get_positive_integer(response: str) -> int:
    """
    parse a string into an int

    The calls to the conversion will throw an exception
    of ValueError if it fails to parse correctly.
    """
    result_int: int = int(response)
    if result_int < 0:
        raise ValueError
    return result_int

def main() -> None:
    """
    Input a string, convert to an integer and print it.
    """

    # Print a welcome message to the screen
    print("Welcome to the get an integer program.")

    input_text: str = input("Enter a positive integer: ")
    try:
        number: int = get_positive_integer(input_text)
        print(f"You entered {number}, which is a positive integer")
    except ValueError:
        print(f"{input_text} is not a positive integer")

    print("Done!")

# This code runs only when the module is executed directly.
if __name__ == '__main__':
    main()
