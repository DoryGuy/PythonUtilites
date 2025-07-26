# Use inheritence to create a JSON Encoder and Decoder for unique objects and classes.

## Overview
In this project, we will create a JSON Encoder and Decoder that can handle custom classes and objects. This is useful
when you want to serialize and deserialize complex data structures that are not natively supported by the JSON module in
Python.

We use a combination of inheritance and custom methods to extend the functionality of the JSON module. The inheritance
allows us to create specialized encoders and decoders for code which we do not have control over, such as complex,
Decimal, and range.

We use a fixed naming convention for the classes, 'to_json' for the encoder and 'from_json' for the decoder in the
classes we create. Then we use a register annotation to register the classes with the JSON module. This allows a
seperation of concerns, where the JSON module is responsible for the serialization and deserialization, while our
classes are responsible for the data structure and logic.

## Usage
Note: This example is not how to implement an employee classes, payscale type does not change the type of employee it is.
Just an example of how to use the JSON Encoder and Decoder for a inheritance class.

```python
from dataclasses import dataclass
from decimal import Decimal 
import json

@dataclass(kw_only=True)
class Employee:
    employee_id: str = ""
    name: str = ""
    pay_scale: Decimal = Decimal(0)

@dataclass(kw_only=True)
@json_class_registry.register
class PartTimeFaculty(Employee):

    def to_json(self) -> str:
        return json.dumps(self.__dict__,
                          sort_keys = True,
                          cls=MyJsonEncoder)

    @classmethod
    def from_json(cls, json_stuff):
        # pylint: disable=possibly-used-before-assignment
        if isinstance(json_stuff, (bytes, bytearray, str)):
            data = json.loads(json_stuff, cls=MyJsonDecoder)
        elif isinstance(json_stuff, dict):
            data = json_stuff
        return cls(**data)

@dataclass(kw_only=True)
@json_class_registry.register
class SalaryEmployee(Employee):
    def to_json(self) -> str:
        return json.dumps(self.__dict__,
                          sort_keys = True,
                          cls=MyJsonEncoder)

    @classmethod
    def from_json(cls, json_stuff):
        # pylint: disable=possibly-used-before-assignment
        if isinstance(json_stuff, (bytes, bytearray, str)):
            data = json.loads(json_stuff, cls=MyJsonDecoder)
        elif isinstance(json_stuff, dict):
            data = json_stuff
        return cls(**data)
```

To handle the Decimal type we do the following:

```python
from decimal import Decimal

from json_extensions import ExtendedJsonEncoder, ExtendedJsonDecoder

class MyJsonEncoder(ExtendedJsonEncoder):
    def encode_Decimal(self, d): # pylint: disable=invalid-name
        return {"value": str(d)}

class MyJsonDecoder(ExtendedJsonDecoder):
    def decode_Decimal(self, obj): # pylint: disable=invalid-name
        return Decimal(obj["value"])
```

This will read and write a list of employee JSON objects like this:

```json
"employees": {
"1" : {
    "__extended_json_type__": "PartTimeFaculty",
     "value": "{
            \"employee_id\": \"12345\",
            \"name\": \"John Doe\",
            \"pay_scale\": { \"__extended_json_type__\": \"Decimal\", \"value\": \"5000.00\"}
        }",
"2" : {
    "__extended_json_type__": "SalaryEmployee",
     "value": "{
            \"employee_id\": \"23456\",
            \"name\": \"Jane Doe\",
            \"pay_scale\": { \"__extended_json_type__\": \"Decimal\", \"value\": \"250000.00\"}
        }"
```

## Conclusion
This is by far the easiest and most flexible way to encode data into JSON objects in Python. You can easily extend this to handle any
type without it becoming too cumbersome.  You may not need all this complexity, but it is a good example of how to use
the python JSON module to handle custom classes and objects.

## src Files

### [class_holder.py](../decorators/src/class_holder.py)
Same file as from the decorators src.
The class that does the annotation of the classes to be collected

### [json_encoders_decoders.py](src/json_encoders_decoders.py)
A custom JSON encoder and decoder that handles the serialization and deserialization of complex, Decimal and range objects.

### [json_extensions.py](src/json_extensions.py)
A custom JSON encoder and decoder that handles the serialization and deserialization of classes registered with the
`json_class_registry` and those in `json_encoders_decoders.py`.

### [json_register.py](../decorators/src/json_register.py)
Same file as from the decorators src.
A registry that holds the classes that can be serialized to JSON. It provides methods to register classes.

## example Files
### [employee.py](example/employee.py)
A group of employee classes that can be serialized to JSON

### [main.py](../basic/example/main.py)
Same file as from the basic example
A simple example of how to read and write JSON files using the custom JSON encoder and decoder.

### [management.py](example/management.py)
A class to hold a dictionary of employees.

### [save_employees.py](example/save_employees.py)
A couple of functions to save and load employees to and from a JSON file.
