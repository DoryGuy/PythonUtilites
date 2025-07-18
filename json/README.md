# JSON  classes to encode Decimal into JSON

## [json_decimal.py](src/json_decimal.py)
This module provides a custom JSON encoder and decoder for handling Python's `Decimal` type. It ensures that `Decimal`
objects are serialized to JSON as string, and can be read back into `Decimal` objects from JSON strings.

It is a good example of how to extend the JSON serialization and deserialization process in Python.

### Example Usage
```python
from decimal import Decimal
import json

from json_decimal import JasonDecimalDecoder, JsonDecimalEncoder

class TestData:
    data: Decimal

    def to_json(self):
        return json.dumps(self, cls=JsonDecimalEncoder)

    @classmethod
    def from_json(cls, json_str):
        return json.loads(json_str, cls=JsonDecimalDecoder)
```

## example
A simple example of how to create a json module to serialize and deserialize a class containing a custom class.
field.
