#
# pylint: disable=line-too-long, invalid-name, bare-except
#
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
        assert(d == d_expected)

        d_j_data = json.dumps(d_expected, cls=JsonDecimalEncoder)

        assert(j_data == d_j_data)
