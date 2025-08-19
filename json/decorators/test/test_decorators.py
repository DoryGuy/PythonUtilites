#
# pylint: disable=line-too-long, invalid-name, bare-except
#
""" Unit test for decorators """

import unittest
import json

from dataclasses import dataclass

from json_encoders_decoders import MyJsonEncoder, MyJsonDecoder
from json_register import json_class_registry


@dataclass(kw_only=True)
@json_class_registry.register
class MyClass():
    """ A test class """
    x: int = int(13)
    y: int = int(6)

    def to_json(self) -> str:
        """ dump to json """
        return json.dumps(self,
                          sort_keys = True,
                          cls=MyJsonEncoder)

    @classmethod
    def from_json(cls, json_stuff):
        """ from a json dict """
        # pylint: disable=possibly-used-before-assignment
        if isinstance(json_stuff, (bytes, bytearray, str)):
            data = json.loads(json_stuff, cls=MyJsonDecoder)
        elif isinstance(json_stuff, dict):
            data = json_stuff
        return cls(**data)

@dataclass(kw_only=True)
@json_class_registry.register
class MyContainer():
    """ test class """
    def __init__(self,y) -> None:
        self.y = y

    def to_json(self) -> str:
        """ dump to json """
        return json.dumps(self,
                          sort_keys = True,
                          cls=MyJsonEncoder)

    @classmethod
    def from_json(cls, json_stuff):
        """ from a json dict """
        # pylint: disable=possibly-used-before-assignment
        if isinstance(json_stuff, (bytes, bytearray, str)):
            data = json.loads(json_stuff, cls=MyJsonDecoder)
        elif isinstance(json_stuff, dict):
            data = json_stuff
        return cls(**data)

class TestOneClassInt (unittest.TestCase):
    """
    Unit Test class for one level
    """

    def test_1(self) -> None:
        """ test with one int """

        j_data = '{"__ClassName__":"MyClass","value":{"x":13, "y":6}}'
        d = json.loads(j_data,cls=MyJsonDecoder)
        d_expected = int(13)
        assert d_expected == d.x

        d_j_data = d.to_json()

        assert j_data == d_j_data


class TestBasicDecoratorInt (unittest.TestCase):
    """
    Unit Test class for basic encoder and decoder
    """

    def test_1(self) -> None:
        """ test with one class with one int """

        j_data = '{"__ClassName__":"MyContainer","value":{"y":{"__ClassName__":"MyClass","value":{"x":15,"y":16}}}}'
        d = json.loads(j_data,cls=MyJsonDecoder)
        d_expected = int(15)
        assert d_expected == d.y.x

        d_j_data = d.to_json()

        assert j_data == d_j_data
