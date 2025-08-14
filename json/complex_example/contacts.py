'''
A class to hold a contact. (demo)
'''



from dataclasses import dataclass
from json_decorators import json_decorator
from json_encoders_decoders import MyJsonEncoder, MyJsonDecoder
from json_register import json_class_registry

@dataclass(kw_only=True)
class Contact:
    ''' contact class '''

@json_class_registry.register
@dataclass(kw_only=True)
@json_decorator(encoder=MyJsonEncoder, decoder=MyJsonDecoder, indent=4, sort_keys=True)
class Email(Contact):
    ''' Email class '''
    address: str = ""

@json_class_registry.register
@dataclass(kw_only=True)
@json_decorator(encoder=MyJsonEncoder, decoder=MyJsonDecoder, indent=4, sort_keys=True)
class Phone(Contact):
    ''' Phone class '''
    type: str = ""
    number: str = ""
