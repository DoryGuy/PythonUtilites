#
# pylint: disable=line-too-long, invalid-name, bare-except
#
""" Unit test for decorators """

import unittest
import json

from dataclasses import dataclass, field

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

    def to_json(self) -> dict:
        """ return a dict for json serialization """
        return {'x': self.x, 'y': self.y, 'z': self.z}

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
    y :MyClass = field(default_factory=lambda: MyClass(0,0,0))   # pylint: disable=unnecessary-lambda

    def __init__(self,y: MyClass) -> None:
        self.y = y

    def to_json(self) -> dict:
        """ return a dict for json serialization """
        return {'y': self.y}

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

        d_j_data = json.dumps(d, cls=MyJsonEncoder, sort_keys=True)

        assert j_data == d_j_data

    def test_2(self) -> None:
        """ test with create json """

        j_data = '{"__ClassName__": "MyClass", "value": {"x": 14, "y": 16, "z": 19}}'
        d = MyClass(14,16,19)
        j = json.dumps(d, cls=MyJsonEncoder, sort_keys=True)

        assert j_data == j

        d2 = MyClass.from_json(j_data)
        d3 = json.loads(j, cls=MyJsonDecoder)
        assert d2 == d3

    def test_3(self) -> None:
        """ test my container """
        mc = MyClass(2,3,4)
        d = MyContainer(mc)

        data_j = json.dumps(d, cls=MyJsonEncoder, sort_keys=True)
        j_data = '{"__ClassName__": "MyContainer", "value": {"y": {"__ClassName__": "MyClass", "value": {"x": 2, "y": 3, "z": 4}}}}'
        assert data_j == j_data

class TestBasicTest (unittest.TestCase):
    """
    Unit Test class for basic encoder and decoder
    """

    def test_1(self) -> None:
        """ test with basic data """

        j_data = '10'

        d = json.loads(j_data, cls=MyJsonDecoder)
        d_expected = 10
        assert d == d_expected

        d_j_data = json.dumps(d_expected, cls=MyJsonEncoder)

        assert j_data == d_j_data

    def test_2(self) -> None:
        """ test with basic data """

        j_data = '"foobar"'

        d = json.loads(j_data, cls=MyJsonDecoder)
        d_expected = "foobar"
        assert d == d_expected

        d_j_data = json.dumps(d_expected, cls=MyJsonEncoder)

        assert j_data == d_j_data

class TestBasicDecoratorInt (unittest.TestCase):
    """
    Unit Test class for basic encoder and decoder
    """

    def test_1(self) -> None:
        """ test with one class with two ints """

        j_data = '{"__ClassName__": "MyContainer", "value": {"y": {"__ClassName__": "MyClass", "value": {"x": 15, "y": 16, "z": 17}}}}'
        d = json.loads(j_data,cls=MyJsonDecoder)
        d_expected_x = int(15)
        assert d_expected_x == d.y.x
        d_expected_z = int(17)
        assert d_expected_z == d.y.z

        d_j_data = json.dumps(d, cls=MyJsonEncoder, sort_keys=True)

        assert j_data == d_j_data

    def test_2(self) -> None:
        """ test with one class two ints. """

        d = MyClass(13,6,11)
        c = MyContainer(d)

        j = json.dumps(c, cls=MyJsonEncoder, sort_keys=True)
        expected = '{"__ClassName__": "MyContainer", "value": {"y": {"__ClassName__": "MyClass", "value": {"x": 13, "y": 6, "z": 11}}}}'
        assert j == expected


@json_class_registry.register
class ClassWithSecret():
    """
    A test class that has a secret field which should NOT be serialized.
    The to_json method excludes the secret, so if to_json is called correctly,
    the secret will not appear in the JSON output.
    """
    def __init__(self, name: str, secret: str):
        self.name = name
        self.secret = secret  # should NOT be serialized

    def to_json(self) -> dict:
        """ Return only the name, excluding the secret """
        return {'name': self.name}

    @classmethod
    def from_json(cls, json_stuff):
        """ Reconstruct from json dict """
        if isinstance(json_stuff, dict):
            # When deserializing, secret is not available, use placeholder
            return cls(name=json_stuff['name'], secret='')
        return None


class TestToJsonPriority(unittest.TestCase):
    """
    Unit tests to verify that to_json() method takes priority over __dict__.
    This is critical for classes that need to exclude sensitive fields or
    customize their JSON representation.
    """

    def test_to_json_excludes_secret_field(self) -> None:
        """
        Test that to_json() is called instead of __dict__, ensuring
        the secret field is NOT included in the JSON output.
        """
        obj = ClassWithSecret(name="test_user", secret="super_secret_password")

        # Encode to JSON
        j = json.dumps(obj, cls=MyJsonEncoder)

        # Verify secret is NOT in the output
        self.assertNotIn("super_secret_password", j)
        self.assertNotIn("secret", j)

        # Verify name IS in the output
        self.assertIn("test_user", j)
        self.assertIn("name", j)

    def test_to_json_round_trip(self) -> None:
        """
        Test that encoding and decoding works correctly when to_json()
        returns a subset of fields.
        """
        obj = ClassWithSecret(name="alice", secret="password123")

        # Encode to JSON
        j = json.dumps(obj, cls=MyJsonEncoder)

        # Decode from JSON
        decoded = json.loads(j, cls=MyJsonDecoder)

        # Verify the name was preserved
        self.assertEqual(decoded.name, "alice")

        # Verify the secret was not serialized (should be empty after round-trip)
        self.assertEqual(decoded.secret, '')
