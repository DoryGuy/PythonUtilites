 # pylint: disable=too-few-public-methods,invalid-name
""" Class to add default to_json and from_json """

from  functools import partial
import json
from json_convert import convert_to_json

class json_decorator:
    """ class to add default Json read and write. fns. """
    def __init__(self, *, encoder = None, decoder = None) -> None:
        """ init the class """
        self.encoder = encoder
        self.decoder = decoder

    def __call__(self, cls):
        """ this method is called when the decorator is applied to the class
        cls is the class being decorated """

        self.add_to_json(cls, self.encoder)
        self.add_from_json(cls, self.decoder)

    def to_json(self,*,encoder) -> str:
        """ dump to json """
        return json.dumps(convert_to_json(self),
                          sort_keys = True,
                          indent=4,
                          cls=encoder)

    def add_to_json(self,cls,encoder) -> None:
        """ add the to_json fn if it doesn't exist """
        if not hasattr(cls,"to_json") and self.encoder is not None:
            setattr(cls, "to_json", partial(self.to_json, encoder=encoder))

    def from_json(cls,json_stuff,*,decoder):
        """ from a json dict """
        # pylint: disable=possibly-used-before-assignment
        if isinstance(json_stuff, (bytes, bytearray, str)):
            data = json.loads(json_stuff, cls=decoder)
        elif isinstance(json_stuff, dict):
            data = json_stuff
        return cls(**data)

    def add_from_json(self, cls, decoder):
        """ add a static class member from_json """
        if not hasattr("from_json") and self.decoder is not None:
            setattr(cls, "from_json", classmethod(partial(self.from_json, decoder=decoder)))
