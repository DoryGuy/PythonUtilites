# Complex Example

### Overview

### Usage

### Conclusion
This technique is a combination of the other techniques used in the [decorators](../decorators) and the [extensions](../extensions)
and the [recursive](...recursive) to make easy to maintain classes that have complex data structures.

### Files

### [address.py](address.py)
A class that holds the fields for an address.

### [class_holder.py](../decorators/src/class_holder.py)
Same file as from the decorators src.

The class that does the annotation of the classes to be collected

### [contacts](contacts)
A class that holds a variety of employee contact classes.

## [employee.py](employee.py)
A group of employee classes that can be serialized to JSON

## [json_convert.py](../recursive/src/json_convert.py)
Same file as from the recursive src

The recursive function to walk the data tree of an object.

### [json_encoders_decoders.py](src/json_encoders_decoders.py)
Same file as from the extensions src

A custom JSON encoder and decoder that handles the serialization and deserialization of complex, Decimal and range objects.

### [json_extensions.py](src/json_extensions.py)
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
