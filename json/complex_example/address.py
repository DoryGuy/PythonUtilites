'''
A class to hold an address. (demo)
'''


from dataclasses import dataclass

@dataclass(kw_only=True)
class Address:
    ''' USA address class '''
    street1: str = ""
    street2: str = ""
    city: str = ""
    state: str = ""
    zip: str = ""
