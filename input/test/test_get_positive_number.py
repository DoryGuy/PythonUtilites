#
# pylint: disable=line-too-long, invalid-name, bare-except
#
'''
# Exercise No.  Hw6 Project 2
# File Name:    hw6TestGetNumber.py
# Programmer:   Gary Powell
# Date:         Feb 16, 2025
#
# Problem Statement: use pytest to test the various input cases
#   for the hw6GetNumber.py
#   use pytest -rxP  hw6TestGetNumber.py to run the tests.
#
# Overall Plan:
# 1. call get_positive_number with a variety of inputs
# 2. Assert that the input is converted correctly to a number
'''
# import the necessary python libraries and the code to test.
import unittest
from get_positive_number import get_positive_number

class TestGetNumber (unittest.TestCase):
    '''
    Unit test class for get_positive_number
    '''

    def test_get_int(self) -> None:
        '''
        test get int
        '''
        response = get_positive_number("1")
        assert isinstance(response, int)
        assert response == 1

    def test_get_float(self) -> None:
        '''
        test get float
        '''
        response = get_positive_number("2.1")
        assert isinstance(response, float)
        assert response ==  2.1

    def test_get_complex(self) -> None:
        '''
        test get complex
        '''
        response = get_positive_number("3+3j")
        assert isinstance(response, complex)
        assert response == 3+3j

        response = get_positive_number("4.0+2j")
        assert isinstance(response, complex)
        assert response == 4.0+2j

        response = get_positive_number("1+2.2j")
        assert isinstance(response, complex)
        assert response == 1+2.2j

        response = get_positive_number("1e3+2.2j")
        assert isinstance(response, complex)
        assert response == 1e3+2.2j


    def test_get_bad_text(self) -> None:
        '''
        test get bad text
        '''
        try:
            _ = get_positive_number("Foo")
            assert False
        except ValueError:
            # we expect only this isinstance of error.
            assert True
        except:
            assert False

    def test_get_scientific(self) -> None:
        '''
        test get scientific
        '''
        response = get_positive_number("1e1")
        assert isinstance(response, float)
        assert response == 10

    def test_get_negative_int(self) -> None:
        '''
        test get negative int
        '''
        try:
            _ = get_positive_number("-5")
        except ValueError:
            # we expect only this isinstance of error.
            assert True

    def test_get_negative_float(self) -> None:
        '''
        test get negative float
        '''
        try:
            _ = get_positive_number("-5.1")
        except ValueError:
            # we expect only this isinstance of error.
            assert True

    def test_get_negative_complex(self) -> None:
        '''
        test get negative complex
        '''
        try:
            _ = get_positive_number("-5.1+1j")
        except ValueError:
            # we expect only this isinstance of error.
            assert True
