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
        if hasattr(obj, '__class__') and obj.__class__.__name__ in json_class_registry.classes:
            if hasattr(obj, 'to_json') and callable(obj.to_json):
                return {'__ClassName__': obj.__class__.__name__, 'value': obj.to_json()}
            raise AttributeError(f"Class {obj.__class__.__name__} does not have a callable to_json method.")
        if hasattr(obj, '__dict__'):
            return obj.__dict__

        return super().default(obj)

class MyJsonDecoder(json.JSONDecoder):
    """ convert JSON to classes """

    def __init__(self, *args, **kwargs):
        """ initialize the class """
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, obj):  # pylint: disable=E0202
        """ override the object_hook member fn """
        if '__ClassName__' in obj:
            try:
                c = json_class_registry.classes[obj['__ClassName__']]
                if hasattr(c, 'from_json') and callable(c.from_json):
                    return c.from_json(obj['value'])
                raise AttributeError(f"Class {obj['__ClassName__']} does not have a callable from_json method.")
            except KeyError:
                raise AttributeError(f"Class {obj['__ClassName__']} is not registered in json_class_registry.")

        return obj
