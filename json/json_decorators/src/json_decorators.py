# pylint: disable=too-few-public-methods,invalid-name,line-too-long
""" Class to add default to_json and from_json """

from  functools import partial
import json
from json_convert import convert_to_json

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

        #assert hasattr(cls, 'to_json')
        #assert hasattr(cls, 'from_json')
        return cls

    def to_json_2(self,**kwargs) -> str:
        """ dump to json """
        return json.dumps(convert_to_json(self),
                          **kwargs)

    def to_json_3(self,**kwargs) -> str:
        """ dump to json """
        return json.dumps(convert_to_json(self),
                          cls=self.encoder,
                          **kwargs)

    def add_to_json(self,cls):
        """ add the to_json fn if it doesn't exist """
        if not hasattr(cls,"to_json"):
            if self.encoder is not None:
                #setattr(cls, "to_json", partial(self.to_json_3, self.encoder, kwargs=self.kwargs))
                setattr(cls, "to_json", lambda x: self.to_json_3(x, self.encoder, kwargs=self.kwargs))
            else:
                setattr(cls, "to_json", partial(self.to_json_2, kwargs=self.kwargs))

        return cls

    def from_json_2(cls,json_stuff):     # pylint: disable=no-self-argument
        """ from a json dict """
        # pylint: disable=possibly-used-before-assignment
        if isinstance(json_stuff, (bytes, bytearray, str)):
            data = json.loads(json_stuff)
        elif isinstance(json_stuff, dict):
            data = json_stuff
        return cls(**data)

    def from_json_3(cls, json_stuff, decoder):     # pylint: disable=no-self-argument
        """ from a json dict """
        # pylint: disable=possibly-used-before-assignment
        if isinstance(json_stuff, (bytes, bytearray, str)):
            data = json.loads(json_stuff, cls=decoder)
        elif isinstance(json_stuff, dict):
            data = json_stuff
        return cls(**data)

    def add_from_json(self, cls):
        """ add a static class member from_json """
        if not hasattr(cls, "from_json"):
            if self.decoder is not None:
                #setattr(cls, "from_json", classmethod(partial(self.from_json_3, self.decoder)))
                cls.from_json = classmethod(lambda cls, js: json_decorator.from_json_3(cls, js, self.decoder))
            else:
                #setattr(cls, "from_json", classmethod(self.from_json_2))
                cls.from_json =  classmethod(json_decorator.from_json_2)

        return cls
