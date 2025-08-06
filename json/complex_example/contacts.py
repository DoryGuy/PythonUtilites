'''
A class to hold a contact. (demo)
'''



from dataclasses import dataclass
import json
from json_register import json_class_registry

@dataclass(kw_only=True)
class Contact:
    ''' contact class '''

@json_class_registry.register
@dataclass(kw_only=True)
class Email(Contact):
    ''' Email class '''
    address: str = ""

    def to_json(self) -> str:
        """ dump to json """
        return json.dumps(self.__dict__,sort_keys=True,indent=4)

    @classmethod
    def from_json(cls, json_stuff):
        """ create a Phone Contact from json """
        # pylint: disable=possibly-used-before-assignment
        if isinstance(json_stuff, (bytes, bytearray, str)):
            data = json.loads(json_stuff)
        elif isinstance(json_stuff, dict):
            data = json_stuff
        return cls(**data)



@json_class_registry.register
@dataclass(kw_only=True)
class Phone(Contact):
    ''' Phone class '''
    type: str = ""
    number: str = ""


    def to_json(self) -> str:
        """ dump to json """
        return json.dumps(self.__dict__,sort_keys=True,indent=4)

    @classmethod
    def from_json(cls, json_stuff):
        """ create a Phone Contact from json """
        # pylint: disable=possibly-used-before-assignment
        if isinstance(json_stuff, (bytes, bytearray, str)):
            data = json.loads(json_stuff)
        elif isinstance(json_stuff, dict):
            data = json_stuff
        return cls(**data)
