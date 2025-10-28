#
# pylint: disable=line-too-long, invalid-name, bare-except
#
""" Unit test for decorators """

import unittest
from dataclasses import dataclass,field
from decimal import Decimal
import json


from json_decorators import json_decorator
from json_encoders_decoders import MyJsonEncoder, MyJsonDecoder
from json_register import json_class_registry


@dataclass(kw_only=True)
@json_class_registry.register
@json_decorator(encoder=MyJsonEncoder,decoder=MyJsonDecoder, indent=4, sort_keys=True)
class MyClass():
    """ A test class """
    #pylint: disable=unnecessary-lambda
    x: Decimal = field(default_factory=lambda: Decimal(13))

@dataclass(kw_only=True)
@json_class_registry.register
@json_decorator(encoder=MyJsonEncoder,decoder=MyJsonDecoder, indent=4, sort_keys=True)
class MyContainer():
    """ test container class """
    #pylint: disable=unnecessary-lambda
    y: MyClass = field(default_factory=lambda: MyClass())

class TestOneClassDecimal (unittest.TestCase):
    """
    Unit Test class for one level
    """

    def test_1(self) -> None:
        """ test with one Decimal """

        j_data = '{"__extended_json_type__": "MyClass", "value": {"x": {"__extended_json_type__": "Decimal", "value": "13"}}}'
        d = json.loads(j_data,cls=MyJsonDecoder)
        d_expected = MyClass()
        assert d_expected == d

        x = MyClass()
        assert hasattr(x, 'to_json')
        assert callable(getattr(x, 'to_json'))

        d_j_data = d.to_json()

        assert j_data == d_j_data

class TestBasicDecoratorDecimal (unittest.TestCase):
    """
    Unit Test class for basic encoder and decoder
    """

    def test_1(self) -> None:
        """ test with one Decimal """
        j_data = '{"__extended_json_type__": "MyContainer", "value": {"y": {"__extended_json_type__": "MyClass", "value": {"x": {"__extended_json_type__": "Decimal","value": "13"}}}}}'
        x = MyContainer()
        assert hasattr(x, 'to_json')
        assert callable(getattr(x, 'to_json'))

        x_data = x.to_json()

        assert j_data == x_data

        d = json.loads(j_data,cls=MyJsonDecoder)
        d_expected = Decimal(13)
        assert d_expected == d.y.x
