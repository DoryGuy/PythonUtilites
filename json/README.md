# Json Utilies for Python

## Overview
The python documentation [JSON encoder and decoder](https://docs.python.org/3/library/json.html) is 
notoriously difficult to understand how to actually use the json module for anything but
basic data or simple objects like complex. I ended up needing to use json to write a class that inherited from a base
class, and had a Decimal field.  My first attempt was pretty awful but it worked well enough.

I have since found much better ways to do this, and I have written a few utilities that make it much easier to work with
json in python for the future projects.

As I find other ways of improving using python to read and write Json I'll update this resource.

## [basic](basic)
Basic is just that, a basic json utility to write out a Decimal field in a class. There is a an example of how to use it, and
a terrible example of a way to also write the classes holding it. (A series of if statements to check the type of the field, one for 
each class type that needs to be serialized, deserialized)

This is the closest to the python documentation which nearly always uses `complex` as the example.

## [decorators](decorators)
This library uses a decorator to note the classes that need to be serialized, it separates the serialization and deserialization
from the Json Encoder and Decoder.  This allows for a cleaner separation of concerns, and makes it easier to
maintain. It also allows for easier expansion of the project in the future, as new classes can be added without breaking
existing code.

It's pretty easy to use, just add the @json_class_registry.register decorator to the class you want to serialize.
And include a `to_json` method that returns a dictionary of the fields you want to serialize, and a `from_json` method
that takes a dictionary and returns an instance of the class. The `json_class_registry` remembers the class and the
json_enoder and decoder will handle the serialization and deserialization of the class automatically.

Of course you still need to handle the unique fields within the class, and that's yet another encoder/decoder that
the class has to provide.  As you can see with classes with a lot of unique fields, this can get a bit ugly fast.
In this example I reuse the basic version of the `json_decimal` for the decimal field.

## [extensions](extensions)
This library came from a blog post here:
https://mathspp.com/blog/custom-json-encoder-decoder
I changed some of the underlying code because I don't like throwing exceptions when I could have tested for a thing.
And I added my decorator code to the ExtendedJsonEncode/Decode functions. But the underlying concept for handling types
where you do not have the source code comes from this blog by Rodrigo.

This is a more advanced version of the decorators, that allows for more complex serialization and deserialization of a
class and types for which we do not control the source code. It relies on the use of `to_json` and `from_json` methods
to serialize and deserialize the classes we write. 

Then for the types for which we do not control the source code, we provide a custom encoder decoder that inherits from
the base classes `ExtendedJsonEncoder`, and `ExtendedJsonDecoder`, and then add member functions to handle the types we want
with the special name `encode_<type>` and `decode_<type>` where `<type>` is the name of the type we are dealing with.
ie `encode_Decimal` and `decode_Decimal` for the Decimal type, `encode_complex`, `decode_complex` etc.


## [recursive](recursive)
This library is from this blog post:
https://www.geeksforgeeks.org/python/python-to-generate-dynamic-nested-json-string

It uses a simple recursive function to walk the data structure and thus handles lists and dictionaries.
The example provided also uses the Decimal field to show how this technique can be combined with the
basic technique to handle custom fields.

## [json_decorators](json_decorators)
This library uses a decorator to generate a 'to_json' member function and a class method 'from_json' from the boiler
plate code found in json_decorotors.  It's to help eliminate repetitive coding and thus reduce bugs.
It relies on techniques from the decorators and the extensions libraries.

This is the most advanced version of the utilities, and is the one I use in my projects. It uses some fancy pants
patterns from python ie. annotations, so might not be the easiest to understand at first, but it is the most powerful and flexible and it's
the easiest to use.

The code in the library looks complex and yet makes it easy to add modules to handle things like datetime, range, complex etc.
So that your code is easy to read and maintain.

Just follow the code in the examples directory, and you will see how to use it.

## [complex_example](complex_example)
Using a more complex employee class, I used the above techniques to create JSON read and writing
functions. This example uses the decorators library, the extensions library, json_decorators and the recursive library.

There is a List of contacts, of which the Contact class uses inheritence, an Address class which is a basic
data structure, and a Name class also a basic data structure.  The Employee class uses the same inheritence
as the basic example.
