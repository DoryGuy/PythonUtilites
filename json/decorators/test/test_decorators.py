#
# pylint: disable=line-too-long, invalid-name, bare-except
#
""" Unit test for decorators """

import unittest
import json

from dataclasses import dataclass, field
from multiprocessing.connection import default_family

from json_encoders_decoders import MyJsonEncoder, MyJsonDecoder
from json_register import json_class_registry


@dataclass
@json_class_registry.register
class MyClass():
    """ A test class """
    x: int
    y: int
    z: int

    def __init__(self, x: int,y: int,z: int):
        self.x = x
        self.y = y
        self.z = z

    def to_json(self) -> str:
        """ dump to json MyClass"""
        return json.dumps(self,
                          sort_keys = True,
                          cls=MyJsonEncoder)

    @classmethod
    def from_json(cls, json_stuff):
        """ from a json dict MyClass"""
        # pylint: disable=possibly-used-before-assignment
        if isinstance(json_stuff, (bytes, bytearray, str)):
            data = json.loads(json_stuff, cls=MyJsonDecoder)
            return data
        if isinstance(json_stuff, dict):
            data = json_stuff

        return cls(**data)

@dataclass
@json_class_registry.register
class MyContainer():
    """ test class """
    y :MyClass = field(default_factory=lambda: MyClass())

    def __init__(self,y: MyClass) -> None:
        self.y = y

    def to_json(self) -> str:
        """ dump to json MyContainer """
        return json.dumps(self,
                          sort_keys = True,
                          cls=MyJsonEncoder)

    @classmethod
    def from_json(cls, json_stuff):
        """ from a json dict MyContainer """
        # pylint: disable=possibly-used-before-assignment
        if isinstance(json_stuff, (bytes, bytearray, str)):
            return json.loads(json_stuff, cls=MyJsonDecoder)
        if isinstance(json_stuff, dict):
            data = json_stuff
        return cls(**data)

class TestOneClassInt (unittest.TestCase):
    """
    Unit Test class for one level
    """

    def test_1(self) -> None:
        """ test with one int """

        j_data = '{"__ClassName__": "MyClass", "value": {"x": 13, "y": 6, "z": 11}}'
        d = json.loads(j_data,cls=MyJsonDecoder)
        d_expected = int(13)
        assert d_expected == d.x

        d_j_data = d.to_json()

        assert (j_data == d_j_data)

    def test_2(self) -> None:
        """ test with create json """

        j_data = '{"__ClassName__": "MyClass", "value": {"x": 14, "y": 16, "z": 19}}'
        d = MyClass(14,16,19)
        j = d.to_json()

        assert j_data == j

        d2 = MyClass.from_json(j_data)
        d3 = MyClass.from_json(j)
        assert (d == d3 )

    def test_3(self) -> None:
        """ test my container """
        mc = MyClass(2,3,4)
        d = MyContainer(mc)

        data_j = d.to_json()
        j_data = '{"__ClassName__": "MyContainer", "value": {"y": {"__ClassName__": "MyClass", "value": {"x": 2, "y": 3, "z": 4}}}}'
        assert data_j == j_data

class TestBasicDecoratorInt (unittest.TestCase):
    """
    Unit Test class for basic encoder and decoder
    """

    def test_1(self) -> None:
        """ test with one class with two ints """

        j_data = '{"__ClassName__": "MyContainer", "value": {"y": {"__ClassName__": "MyClass", "value": {"x": 15, "y": 16, "z": 17}}}}'
        #d = json.loads(j_data,cls=MyJsonDecoder)
        d2 = MyContainer.from_json(j_data)
        d_expected_x = int(15)
        assert d_expected_x == d2.y.x
        #assert d_expected_x == d.y.x
        d_expected_z = int(17)
        #assert d_expected_z == d.y.z

        d_j_data = d2.to_json()

        assert j_data == d_j_data

    def test_2(self) -> None:
        """ test with one class two ints. """

        d = MyClass(13,6,11)
        c = MyContainer(d)

        j = c.to_json()
