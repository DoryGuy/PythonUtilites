#! /usr/bin/python
#
# pylint: disable=line-too-long,invalid-name
#
"""
# Exercise No.   Hw13 extra credit
# File Name:     get_integer.py
# Programmer:    Gary Powell
# Date:          May 1, 2025
#
# Problem Statement: convert a string to an int
#   Check for bad inputs.
#
#
# Overall Plan:
"""
# import the necessary python libraries

def get_integer(response: str) -> int:
    """
    parse a string into an int

    The calls to the conversion will throw an exception
    of ValueError if it fails to parse correctly.
    """
    result_int: int = int(response)
    return result_int

def main() -> None:
    """
    Input a string, convert to an integer and print it.
    """

    # Print a welcome message to the screen
    print("Welcome to the get an integer program.")

    input_text: str = input("Enter an integer: ")
    try:
        number: int = get_integer(input_text)
        print(f"You entered {number}, which is an integer")
    except ValueError:
        print(f"{input_text} is not an integer")

    print("Done!")

# This code runs only when the module is executed directly.
if __name__ == '__main__':
    main()
