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
@json_decorator(encoder=MyJsonEncoder,decoder=MyJsonDecoder, sort_keys=True)
class MyClass():
    """ A test class """
    #pylint: disable=unnecessary-lambda
    x: Decimal = field(default_factory=lambda: Decimal(13))

@dataclass(kw_only=True)
@json_class_registry.register
@json_decorator(encoder=MyJsonEncoder,decoder=MyJsonDecoder, sort_keys=True)
class MyContainer():
    """ test container class """
    #pylint: disable=unnecessary-lambda
    y: MyClass = field(default_factory=lambda: MyClass(Decimal(14)))

class TestOneClassDecimal (unittest.TestCase):
    """
    Unit Test class for one level
    """

    def test_1(self) -> None:
        """ test with one Decimal """

        j_data = '{"__extended_json_type__": "MyClass", "value": {"x": {"__extended_json_type__": "Decimal", "value": "14"}}}'
        x = MyClass(x=Decimal(14))
        assert hasattr(x, 'from_json')
        assert callable(getattr(x, 'from_json'))

        d = json.loads(j_data,cls=MyJsonDecoder)
        assert hasattr(d, 'to_json')
        assert callable(getattr(d, 'to_json'))
        assert hasattr(d, 'from_json')
        assert callable(getattr(d, 'from_json'))

        d_expected = MyClass(x=Decimal(14))
        assert d_expected == d

        d_j_data = d.to_json()

        assert j_data == d_j_data

class TestBasicDecoratorDecimal (unittest.TestCase):
    """
    Unit Test class for basic encoder and decoder
    """

    def test_1(self) -> None:
        """ test with one MyClass """
        j_data = '{"__extended_json_type__": "MyContainer", "value": {"y": {"__extended_json_type__": "MyClass", "value": {"x": {"__extended_json_type__": "Decimal", "value": "15"}}}}}'
        d = json.loads(j_data,cls=MyJsonDecoder)
        assert hasattr(d, 'to_json')
        assert callable(getattr(d, 'to_json'))

        assert hasattr(d, 'from_json')
        assert callable(getattr(d, 'from_json'))

        d_expected = Decimal(15)
        assert d_expected == d.y.x

        d_data = d.to_json()

        assert j_data == d_data
