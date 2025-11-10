# pylint: disable=too-few-public-methods,invalid-name,line-too-long
""" Class to add default to_json and from_json """

import json
from json_convert import convert_to_json

def to_json_2(self, **kwargs) -> str:
    """ dump to json without a custom encoder """
    if not kwargs:
        return json.dumps(convert_to_json(self))
    return json.dumps(convert_to_json(self),
                          **kwargs)

def to_json_3(self,encoder, **kwargs) -> str:
    """ dump to json with a custom encoder """
    if not kwargs:
        return json.dumps(convert_to_json(self),
                          cls=encoder)
    return json.dumps(convert_to_json(self),
                      cls=encoder,
                      **kwargs)
class json_decorator:
    """ class to add default Json read and write. fns. """
    def __init__(self, *, encoder = None, decoder = None, **kwargs) -> None:
        """ init the class """
        self.encoder = encoder
        self.decoder = decoder
        self.kwargs = kwargs

    def __call__(self, cls):
        """ this method is called when the decorator is applied to the class
        cls is the class being decorated """
        cls = self.add_to_json(cls)
        cls = self.add_from_json(cls)
        return cls

    def add_to_json(self,cls):
        """ add the to_json fn if it doesn't exist """
        if not hasattr(cls,"to_json"):
            if self.encoder is not None:
                setattr(cls, "to_json", lambda x: to_json_3(x, self.encoder, **self.kwargs))
            else:
                setattr(cls, "to_json", lambda x: to_json_2(x, **self.kwargs))

        return cls

    def from_json_2(cls,json_stuff):     # pylint: disable=no-self-argument
        """ from a json dict without a custom decoder"""
        # pylint: disable=possibly-used-before-assignment
        if isinstance(json_stuff, (bytes, bytearray, str)):
            return json.loads(json_stuff)
        if isinstance(json_stuff, dict):
            data = json_stuff
        return cls(**data)

    def from_json_3(cls, json_stuff, decoder):     # pylint: disable=no-self-argument
        """ from a json dict with a custom decoder """
        # pylint: disable=possibly-used-before-assignment
        if isinstance(json_stuff, (bytes, bytearray, str)):
            return json.loads(json_stuff, cls=decoder)
        if isinstance(json_stuff, dict):
            data = json_stuff
        return cls(**data)

    def add_from_json(self, cls):
        """ add a static class member from_json """
        if not hasattr(cls, "from_json"):
            if self.decoder is not None:
                cls.from_json = classmethod(lambda cls, js: json_decorator.from_json_3(cls, js, self.decoder))
            else:
                cls.from_json =  classmethod(json_decorator.from_json_2)
        return cls
