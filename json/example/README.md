# Example

## [json_emloyee.py](json_employee.py)

Given a group of classes that represent an employee types, create a JSON Encoder and Decoder to convert them to and from
JSON.

## [employee.py](employee.py)
A sample group of classes that represent an employee types.

Create a JSON Encoder and Decoder to convert them to and from JSON is not trival, however
if you follow this exmaple, you can make it work for your own classes. The trick is that
you override the default method of the JSONEncoder class and the default method of the JSONDecoder class
with your own test for your own classes. You can't just test for the "to_json" method because if it's the top level
class, it will cause an infinite loop. Instead, you need to test for the class name and then call the that classes
to_json methond.

This way you can at each level have a different override. For instance the json_employee class does not know about the
Decimial type, but each employee class has a field of that type so it's to_json call references the json_decimal class.

Since all of the Employee type classes inherit from the base class Employee we test for that class type and then to see
if it has a to_json method that is callable. If it does, we call it and return the result.
