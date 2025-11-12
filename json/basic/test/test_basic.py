#
# pylint: disable=line-too-long, invalid-name, bare-except
#
""" Unit test code """
import unittest

from decimal import Decimal
import json
from json_decimal import JsonDecimalEncoder, JsonDecimalDecoder

class TestBasicDeimal (unittest.TestCase):
    """
    Unit Test class for basic encoder and decoder
    """

    def test_1(self) -> None:
        """ test with one Decimal """

        j_data = '{"__Decimal__": "1.2"}'

        d = json.loads(j_data, cls=JsonDecimalDecoder)
        d_expected = Decimal('1.2')
        assert d == d_expected

        d_j_data = json.dumps(d_expected, cls=JsonDecimalEncoder)

        assert j_data == d_j_data

    def test_2(self) -> None:
        """ test with basic data """

        j_data = '10'

        d = json.loads(j_data, cls=JsonDecimalDecoder)
        d_expected = 10
        assert d == d_expected

        d_j_data = json.dumps(d_expected, cls=JsonDecimalEncoder)

        assert j_data == d_j_data

    def test_3(self) -> None:
        """ test with basic data """

        j_data = '"foobar"'

        d = json.loads(j_data, cls=JsonDecimalDecoder)
        d_expected = "foobar"
        assert d == d_expected

        d_j_data = json.dumps(d_expected, cls=JsonDecimalEncoder)

        assert j_data == d_j_data
