# Recursive

### Overview
From https://www.geeksforgeeks.org/python/python-to-generate-dynamic-nested-json-string/

We use a recursive function call to handle nested structures. It traverses the input data
converting dictionaries and lists into nested structures.

```python
# Using Recursive Functions
def convert_to_json(obj):
    if isinstance(obj, dict):
        return {key: convert_to_json(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [convert_to_json(item) for item in obj]
    else:
        return obj
```

### Usage

```python
class Name:
    first: str = ""
    last: str = ""
    
class MyClass:
    def __init__(self, name: Name, value):
        self.name: Name = name
        self.value = value

    def to_json(self):
        return json.dumps(convert_to_json(self), sort_keys=True, indent=4)

    @classmethod
    def from_json(cls, data):
        if isinstance(data, (bytes, bytearray, str)):
            data = json.loads(data)
        elif isinstance(data, dict):
            data = data
        return cls(**data)
```

### Conclusion
This technique can be combined with the other techniques like the decorator to make easy to maintain
classes.

### src Files

## [json_convert.py](src/json_convert.py)
The recursive function to walk the data tree of an object.

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

## [name.py](example/name.py)
A simple class to hold a employee name.

## [save_employees.py](../basic/example/save_employees.py)
Same file as the basic example

A couple of functions to save and load employees to and from a JSON file.
