#
# pylint: disable=line-too-long, invalid-name, bare-except
#
"""
# Exercise No.  Hw7 Project 1
# File Name:    hw7TestGetRealNumber.py
# Programmer:   Gary Powell
# Date:         Feb 18, 2025
#
# Problem Statement: use pytest to test the various input cases
#   for the hw7GetPositiveRealNumber.py
#   use pytest -rxP  hw7TestGetPositiveRealNumber.py to run the tests.
#
# Overall Plan:
# 1. call get_positive_real_number with a variety of inputs
# 2. Assert that the input is converted correctly to a number
"""
# import the necessary python libraries and the code to test.
import unittest
from get_positive_real_number import get_positive_real_number


class TestGetPositiveRealNumber (unittest.TestCase):
    """
    Unit test class for get_positive_real_number
    """

    def test_get_positive_int(self) -> None:
        """
        test get int
        """
        response = get_positive_real_number("1")
        assert isinstance(response, int)
        assert response == 1

    def test_get_positive_float(self) -> None:
        """
        test get float
        """
        response = get_positive_real_number("2.1")
        assert isinstance(response, float)
        assert response ==  2.1

    def test_get_positive_complex(self) -> None:
        """
        test get complex
        """
        try:
            _ = get_positive_real_number("3+3j")
            assert False
        except ValueError:
            # we expect only this isinstance of error.
            assert True
        except:
            assert False

    def test_get_bad_text(self) -> None:
        """
        test get bad text
        """
        try:
            _ = get_positive_real_number("Foo")
            assert False
        except ValueError:
            # we expect only this isinstance of error.
            assert True
        except:
            assert False

    def test_get_positive_scientific(self) -> None:
        """
        test get scientific
        """
        response = get_positive_real_number("1e1")
        assert isinstance(response, float)
        assert response == 10

    def test_get_negative_int(self) -> None:
        """
        test get negative int
        """
        try:
            _ = get_positive_real_number("-5")
        except ValueError:
            assert True
        except:
            assert False
