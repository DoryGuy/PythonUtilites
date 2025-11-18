#
# pylint: disable=line-too-long, invalid-name, bare-except
#
"""
# Exercise No.  Hw12 Project 1
# File Name:    test_get_integer.py
# Programmer:   Gary Powell
# Date:         Feb 20, 2025
#
# Problem Statement: use pytest to test the various input cases
#   for the get_integer.py
#   use pytest -rxP  test_get_integer.py to run the tests.
#
# Overall Plan:
# 1. call get_integer_number with a variety of inputs
# 2. Assert that the input is converted correctly to a number
"""
# import the necessary python libraries and the code to test.
import unittest
from get_integer import get_integer

class TestGetInteger (unittest.TestCase):
    """
    Unit test class for get_integer
    """

    def test_get_int(self) -> None:
        """
        test get int
        """
        response = get_integer("1")
        assert isinstance(response, int)
        assert response == 1

    def test_get_float(self) -> None:
        """
        test get float
        """
        try:
            _ = get_integer("2.1")
            assert False
        except ValueError:
            # we expect only this isinstance of error.
            assert True
        except:
            assert False

    def test_get_complex(self) -> None:
        """
        test get complex
        """
        try:
            _ = get_integer("3+3j")
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
            _ = get_integer("Foo")
            assert False
        except ValueError:
            # we expect only this isinstance of error.
            assert True
        except:
            assert False

    def test_get_scientific(self) -> None:
        """
        test get scientific
        """
        try:
            _ = get_integer("1e1")
            assert False
        except ValueError:
            # we expect only this isinstance of error.
            assert True
        except:
            assert False

    def test_get_negative_int(self) -> None:
        """
        test get negative int
        """
        response = get_integer("-5")
        assert isinstance(response, int)
        assert response == -5
