# Custom JSON writing for Python Classes

### Overview
This Python module provides a custom JSON encoder that allows you to serialize Python classes into JSON format. It is
particularly useful for classes that contain non-serializable fields or require special handling during serialization.

It requires that the classes you want to serialize implement a `to_json` method that returns a dictionary representation
of the object, and a `from_json` class method that can create an instance of the class from a dictionary.

It also requires that the classes are annotated with @json_class_registry.register to register them with the JSON 
encoder and decoder.

### Usage

'''python
from json_registry import json_class_registry

@json_class_registry.register
class MyClass:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def to_json(self):
        return json.dumps(self, sort_keys=True, indent=4, cls=JsonCustomEncoder)

    @classmethod
    def from_json(cls, data):
        if isinstance(data, (bytes, bytearray, str)):
            data = json.loads(data, cls =JsonCustomDecoder)
        elif isinstance(data, dict):
            data = data
        return cls(**data)
```


## [class_holder.py](class_holder.py)
The class that does the annotation of the classes to be collected

## [employee.py](employee.py)
A group of employee classes that can be serialized to JSON

## [json_custom.py](json_custom.py)
A custom JSON encoder and decoder that handles the serialization and deserialization of classes registered with the
`json_class_registry`.

## [json_decimal.py](json_decimal.py)
A custom JSON encoder and decoder that handles the serialization and deserialization of Decimal objects.

## [json_registry.py](json_registry.py)
A registry that holds the classes that can be serialized to JSON. It provides methods to register classes.

## [main.py](main.py)
A simple example of how to read and write JSON files using the custom JSON encoder and decoder.

## [management.py](management.py)
A class to hold a dictionary of employees.

## [save_employee.py](save_employee.py)
A couple of functions to save and load employees to and from a JSON file.
