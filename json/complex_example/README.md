# Complex Example

### Overview
Given an Employee class read and write the JSON file. The class has objects which inherit from a base class, a List of 
objects which also inherit from a base class, and a Decimal field which is not part of the JSON offical format.

### Usage
```python
from dataclasses import dataclass, field
from typing import List

from json_decorators import json_decorator
from json_encoders_decoders import MyJsonEncoder, MyJsonDecoder
from json_register import json_class_registry

@dataclass(kw_only=True)
class Address:
    street: str = ""
    city: str = ""
    state: str = ""
    zip: str = ""
    
@dataclass(kw_only=True)
class Name:
    first: str = ""
    last: str = ""

class Contact:
    """ Lots of useful fns. """

@json_class_registry.register
@dataclass(kw_only=True)
@json_decorator()
class Email(Contact):
    address: str = ""

@json_class_registry.register
@dataclass(kw_only=True)
@json_decorator()
class Phone(Contact):
    type: str = ""
    number: str = ""
    
@dataclass(kw_only=True)
@json_decorator(encoder=MyJsonEncoder, decoder=MyJsonDecoder)
class MyEmployeeClass:
    name: Name = field(default_factory=lambda: Name())
    address: Address = field(default_factory=lambda: Address())
    pay_scale: Decimal
    contacts: List[Contact]

    def __init__(self, name: Name, value: Decimal, address: Address, contacts: List[Contact]):
        self.name: Name = name
        self.address = address
        self.pay_scale = value
        self.contacts = contacts
```

Note: The Address, and Name classes don't have to be registered or have custom "to_json" and "from_json" member
functions because they are just data which is part of the JSON standard.

### Conclusion
This technique is a combination of the other techniques used in the [decorators](../decorators) and the [extensions](../extensions)
and the [recursive](...recursive) and the [json_decorators](../json_decorators) to make easy to maintain classes that have complex data structures.

### Files

### [address.py](address.py)
A class that holds the fields for an address.

### [class_holder.py](../decorators/src/class_holder.py)
Same file as from the decorators src.

The class that does the annotation of the classes to be collected

### [contacts.py](contacts.py)
A class that holds a variety of employee contact classes.

### [employee.py](employee.py)
A group of employee classes that can be serialized to JSON

### [json_convert.py](../recursive/src/json_convert.py)
Same file as from the recursive src

The recursive function to walk the data tree of an object.

### [json_encoders_decoders.py](../extensions/src/json_encoders_decoders.py)
Same file as from the extensions src

A custom JSON encoder and decoder that handles the serialization and deserialization of complex, Decimal and range objects.

### [json_extensions.py](../extensions/src/json_extensions.py)
Same file as from the extensions src

A custom JSON encoder and decoder that handles the serialization and deserialization of classes registered with the
`json_class_registry` and those in `json_encoders_decoders.py`.

### [json_register.py](../decorators/src/json_register.py)
Same file as from the decorators src.

A registry that holds the classes that can be serialized to JSON. It provides methods to register classes.

### [main.py](../basic/example/main.py)
Same file as from the basic example

A simple example of how to read and write JSON files using the custom JSON encoder and decoder.

### [management.py](../basic/example/management.py)
Same file as from basic example.

A class to hold a dictionary of employees.

### [name.py](../recursive/example/name.py)
Same file as from the recursive example.

A simple class to hold a name.

### [save_employees.py](../basic/example/save_employees.py)
Same file as from basic example.

A couple of functions to save and load employees to and from a JSON file.
