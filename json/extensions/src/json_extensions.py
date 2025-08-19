#pylint: disable=raise-missing-from
'''
https://mathspp.com/blog/custom-json-encoder-decoder
with some minor modifications

Handles both the Json Extensions, and the classes we have registered.
Does some checking to make sure that there is a to_json and a from_json
member function that is callable.

If you control the source, you could remove those checks for additional speed
and instead use a try/exception block.
'''
# pylint: disable=line-too-long

import json
from json_register import json_class_registry

class ExtendedJsonEncoder(json.JSONEncoder):
    """ convert objects and classes to JSON """
    def __init__(self, *args, **kwargs):
        """ initialize the class """
        self.__prev_obj = None
        super().__init__(*args, **kwargs)

    def default(self, obj):     # pylint: disable=arguments-renamed
        ''' convert objects and classes to JSON '''
        name = type(obj).__name__
        member_fn = f"encode_{name}"
        if hasattr(self, member_fn):
            encoder = getattr(self, member_fn)
            if not callable(encoder):
                raise AttributeError(f"{member_fn} is not a callable fn in the json.JSONEncoder hierarchy")
            encoded = encoder(obj)
            encoded["__extended_json_type__"] = name
            return encoded

        if hasattr(obj, '__class__') and name in json_class_registry.classes:
            if self.__prev_obj is None:
                self.__prev_obj = obj
                if hasattr('obj', '__dict__'):
                    return {'__extended_json_type__': name, 'value': obj.__dict__}
                else:
                    return {'__extended_json_type__': name, 'value': super().default(obj)}
            else:
                if hasattr(obj, 'to_json') and callable(obj.to_json):
                    self.__prev_obj = None
                    return {'__extended_json_type__': name, 'value': obj.to_json()}

                raise AttributeError(f"Class {name} does not have a callable to_json method.")

        if hasattr(obj, '__dict__'):
           return obj.__dict__

        return super().default(obj)

class ExtendedJsonDecoder(json.JSONDecoder):
    """ convert JSON to classes and objects"""

    def __init__(self, *args, **kwargs):
        """ initialize the class """
        self.__prev_obj = None
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, obj):       # pylint: disable=E0202
        """ convert JSON objects to classes and objects """
        if "__extended_json_type__" in obj:
            name = obj["__extended_json_type__"]
            decode_name = f"decode_{name}"
            if hasattr(self, decode_name) and callable(getattr(self, decode_name)):
                decoder = getattr(self, decode_name)
                return decoder(obj)

            try:
                c = json_class_registry[name]
                if hasattr(c, 'from_json') and callable(c.from_json):
                    if self.__prev_obj is not None:
                       self.__prev_obj = None
                       return obj['value']
                    self.__prev_obj = obj
                    return c.from_json(obj['value'])
                raise AttributeError(f"Class {name} does not have a callable from_json method.")
            except KeyError:
                raise AttributeError(f"Class {name} is not registered in json_class_registry or custom_decoder.")
        return obj
