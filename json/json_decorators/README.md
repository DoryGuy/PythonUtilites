# Use a decorator to generate a default to_json and from_json member functions

## Overview

## Usage
Note: This example is not how to implement an employee classes, payscale type does not change the type of employee it is.
Just an example of how to use the JSON Encoder and Decoder for a inheritance class.

```python
from dataclasses import dataclass
from decimal import Decimal
import json

from json_decorators import json_decorator
from json_register import json_class_registry

@dataclass(kw_only=True)
class Employee:
    employee_id: str = ""
    name: str = ""
    pay_scale: Decimal = Decimal(0)

@dataclass(kw_only=True)
@json_class_registry.register
@json_decorator(encoder=MyJsonEncoder,decoder=MyJsonDecoder)
class PartTimeFaculty(Employee):

@dataclass(kw_only=True)
@json_class_registry.register
@json_decorator(encoder=MyJsonEncoder,decoder=MyJsonDecoder)
class SalaryEmployee(Employee):
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
     "value": {
            "employee_id": "12345",
            "name": "John Doe",
            "pay_scale": { "__extended_json_type__": "Decimal", "value": "5000.00"}
        },
"2" : {
    "__extended_json_type__": "SalaryEmployee",
     "value": {
            "employee_id": "23456",
            "name": "Jane Doe",
            "pay_scale": { "__extended_json_type__": "Decimal", "value": "250000.00"}
        }
```

## Conclusion

## src Files
### [class_holder.py](../decorators/src/class_holder.py)
Same file as from the decorators src.

The class that does the annotation of the classes to be collected

### [json_decorator.py](src/json_decorator.py)
A class which will generate if not defined and specified as
an argument to the decorator the member function 'to_json' and a class method 'from_json'.

### [json_encoders_decoders.py](src/json_encoders_decoders.py)
Same file as from the extension src.

A custom JSON encoder and decoder that handles the serialization and deserialization of complex, Decimal and range objects.

### [json_extensions.py](src/json_extensions.py)
Same file as from the extensions src.

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

### [management.py](../basic/example/management.py)
Same file as from basic example.

A class to hold a dictionary of employees.

### [save_employees.py](../basic/example/save_employees.py)
Same file as from basic example.

A couple of functions to save and load employees to and from a JSON file.
