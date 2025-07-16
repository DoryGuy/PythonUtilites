#
# pylint: disable=line-too-long, invalid-name, bare-except
#
'''
# Exercise No.  Final Project 3
# File Name:    test_get_positive_decimal_number.py
# Programmer:   Gary Powell
# Date:         Feb 18, 2025
#
# Problem Statement: use pytest to test the various input cases
#   for the get_positive_decimal_number.py
#   use pytest -rxP  test_get_positive_decimal_number.py to run the tests.
#
# Overall Plan:
# 1. call get_positive_decimal_number with a variety of inputs
# 2. Assert that the input is converted correctly to a decimal number
'''
# import the necessary python libraries and the code to test.
from decimal import Decimal
import unittest
import src
from src.get_positive_decimal_number import get_positive_decimal_number

class TestGetPositiveRealNumber (unittest.TestCase):
    '''
    Unit test class for get_positive_decimal_number
    '''

    def test_get_positive_int(self) -> None:
        '''
        test get int
        '''
        response = get_positive_decimal_number("1")
        assert isinstance(response, Decimal)
        assert response == 1

    def test_get_positive_Decimal(self) -> None:
        '''
        test get Decimal
        '''
        response = get_positive_decimal_number("2.25")
        assert isinstance(response, Decimal)
        assert response == Decimal(2.25)

    def test_get_positive_complex(self) -> None:
        '''
        test get complex
        '''
        try:
            _ = get_positive_decimal_number("3+3j")
            assert False
        except ValueError:
            # we expect only this isinstance of error.
            assert True
        except:
            assert False

    def test_get_bad_text(self) -> None:
        '''
        test get bad text
        '''
        try:
            _ = get_positive_decimal_number("Foo")
            assert False
        except ValueError:
            # we expect only this isinstance of error.
            assert True
        except:
            assert False

    def test_get_positive_scientific(self) -> None:
        '''
        test get scientific
        '''
        response = get_positive_decimal_number("1e1")
        assert isinstance(response, Decimal)
        assert response == 10

    def test_get_negative_int(self) -> None:
        '''
        test get negative int
        '''
        try:
            _ = get_positive_decimal_number("-5")
        except ValueError:
            assert True
        except:
            assert False
