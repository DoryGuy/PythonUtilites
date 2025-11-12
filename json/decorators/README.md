# Custom JSON writing for Python Classes
### Overview
This Python module provides a custom JSON encoder that allows you to serialize Python classes into JSON format. It is
particularly useful for classes that contain non-serializable fields or require special handling during serialization.
This custom encoder and decoder are designed to work with classes that implement a specific interface for JSON
serialization. As we saw in the example, having to test for each class name, and then calling it's constructor is a
pain, if you have a lot of classes to serialize. This module provides a way to register classes with a registry, so that
they can be serialized and deserialized without having to explicitly check for each class name.

The module looks for the two specific member functions `to_json` and `from_json` in the classes that are registered and
uses those methods to serialize and deserialize the objects. This allows for a clean separation of concerns, where the
classes themselves handle their own serialization logic, while the custom JSON encoder and decoder handle the actual
serialization and deserialization process.

It requires that the classes you want to serialize implement a `to_json` member method that returns a dictionary representation
of the object, and a `from_json` class method that can create an instance of the class from a dictionary.

It also requires that the classes are annotated with @json_class_registry.register to register them with the JSON 
encoder and decoder.

### Usage

```python
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
            return json.loads(data, cls=JsonCustomDecoder)
        if isinstance(data, dict):
            data = data
        return cls(**data)
```

### Conclusion
This implementation is more complex, but it's more flexible and allows for a cleaner separation of concerns. And it
makes the classes themselves easier to write and test.

But we can do better, so checkout the [extensions](../extensions)  json module section for a more advanced implementation that handles
multiple types of objects within the class such as Decimal, complex, datetime, and more.


### src Files

## [class_holder.py](src/class_holder.py)
The class that does the annotation of the classes to be collected

## [json_encoders_decoders.py](src/json_encoders_decoders.py)
A custom JSON encoder and decoder that handles the serialization and deserialization of classes registered with the
`json_class_registry`.

## [json_register.py](src/json_register.py)
A registry that holds the classes that can be serialized to JSON. It provides methods to register classes.

### example Files

## [employee.py](example/employee.py)
A group of employee classes that can be serialized to JSON

## [json_decimal.py](../basic/src/json_decimal.py)
Same one from the basic src library

A custom JSON encoder and decoder that handles the serialization and deserialization of Decimal objects.

## [main.py](../basic/example/main.py)
Same one from the basic example

A simple example of how to read and write JSON files using the custom JSON encoder and decoder.

## [management.py](../basic/example/management.py)
Same file as the basic example

A class to hold a dictionary of employees.

## [save_employees.py](../basic/example/save_employees.py)
Same file as the basic example

A couple of functions to save and load employees to and from a JSON file.

## test Files

### [test_decorators.py](test/test_decorators.py)
The unit tests for this library
