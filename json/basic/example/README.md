# Example

## [json_employee.py](json_employee.py)
Given a group of classes that represent an employee types, create a JSON Encoder and Decoder to convert them to and from
JSON.

## [json_decimal.py](json_decimal.py)
A JSON Encoder and Decoder for the Decimal type. This is used by the Employee classes to convert the Decimal type to and
from JSON.

## [employee.py](employee.py)
A sample group of classes that represent an employee types.

## [main.py](main.py)
A main program that creates a group of employees from a JSON file, then writes them back out to a JSON file.

## [management.py](management.py)
A class that holds a dictionary of employees.

## [save_employees.py](save_employees.py)
Two functions that save the employees to a JSON file and read them back in from a JSON file.

### Overview
The basic python json module does not handle custom classes very well. It handles basic types like int, float, str,
list, dict, etc. but not custom classes. If you try to convert a custom class to JSON, you will get a TypeError

In this example, we have a base class `Employee` and three derived classes `FullTimeEmployee`, SalaryEmployee 
and `PartTimeEmployee`. We have a EmployeeManagement class that holds a dictionary of employees. The Employee classes
all derive from a common base class Employee, which has a method `to_json`.

What we want to do is save the dictionary of employees to a JSON file and then read them back in. We are using JSON
because it is a common format for data interchange and is easy to read and write.

The issue is to write out each employee class object to JSON and then read them back in with a minimal of unique code.
As we did with the Decimal class, we write a unique identifier for each class that we want to handle in the JSONEncoder
and JSONDecoder. In this case we use the name of the class with "__" as a prefix and suffix, so for the
`FullTimeEmployee` class, we use the identifier `__FullTimeEmployee__`. This allows us to identify the class when we
read the JSON back in and call the appropriate class method to convert it back to an object.

To create a JSON Encoder and Decoder to convert the classes to and from JSON is not trival, however
if you follow this example, you can make it work for your own classes. The key is that
you override the `default` method of the JSONEncoder class and the `object_hook` method of the JSONDecoder class
with your own tests for your own classes. You can't just test for the "to_json" method in the class because if it's the top level
class, it will cause an infinite loop. Instead, you need to test for the class name and then call the that classes
to_json method.

This way you can at each level have a different override. For instance the json_employee class does not know about the
Decimial type, but each employee class has a field of that type so it's in the to_json call that references 
the json_decimal class.

Since all of the Employee type classes inherit from the base class Employee we test for that base class type and then to see
if it has a to_json method that is callable. If it does, we call it and return the result. This makes adding additional
employee types easy, just add the class with the two methods, and it will be automatically handled by the JSONEncoder.
For the JSONDecoder, we test for the class name and then call the from_json method of that class, so you will have to
add that test to the JSONDecoder as well.


If you have a class with a field that is a custom type, you will need to add a test for that type in the JSONEncoder.
In a cascade of tests for type. ie complex, Decimal etc.

### Conclusion
I found the online documentation for the JSONEncoder and JSONDecoder classes to be a bit sparse, and confusing, so I
created this example for you. And the future me, which can reference this example when I need to do this again.
https://docs.python.org/3/library/json.html

Note: don't create your Employee classes this way. The Employee class should have a payroll object that can handle
different types of employees. You aren't a different employee just because you change the way you are paid.

Also checkout the `extentions` module for a more complete example of how to extend the JSONEncoder and JSONDecoder
classes
