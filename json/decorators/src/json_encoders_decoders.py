#
# pylint: disable=line-too-long
#
"""
# File: json_encoders_decoders.py
# Programmer: Gary Powell
# Date: July 20, 2025
#
# Problem Statement: Classes write data in Json
#
# Overall Plan:
#   Use as much of the json library as possible.
#   minimize the amount of dependency on the classes themselves.

#   To use this module, you need to register the classes with the json_class_registry,
#   and have a "to_json", and "from_json" method in the class.
"""

import json
from json_register import json_class_registry

class MyJsonEncoder(json.JSONEncoder):
    """ convert classes to JSON """

    def default(self,obj):      # pylint: disable=arguments-renamed
        """ override the default """
        name = type(obj).__name__
        if hasattr(obj, '__class__') and name in json_class_registry.classes:
            if hasattr(obj,'items') and callable(obj.items):
                return {'__ClassName__': name, 'value': obj.items()}
            if hasattr(obj, '__dict__'):
                return {'__ClassName__': name, 'value': obj.__dict__}
            if hasattr(obj, 'to_json') and callable(obj.to_json):
                return {'__ClassName__': name, 'value': obj.to_json()}

            raise AttributeError(f"Class {name} does not have a callable to_json method.")

        if hasattr(obj, '__dict__'):
            return obj.__dict__

        return super().default(obj)


class MyJsonDecoder(json.JSONDecoder):
    """ convert JSON to classes """

    def object_hook(self, obj):  # pylint: disable=E0202
        """ override the object_hook member fn """
        if '__ClassName__' in obj:
            try:
                name = obj['__className__']
                c = json_class_registry.classes[name]
                if hasattr(c, 'from_json') and callable(c.from_json):
                    return c.from_json(obj['value'])
                raise AttributeError(f"Class {name} does not have a callable from_json method.")
            except KeyError:
                raise AttributeError(f"Class {name} is not registered in json_class_registry.")
        return obj
