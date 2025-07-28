'''
A class to hold a name. (demo)
'''


from dataclasses import dataclass

@dataclass(kw_only=True)
class Name:
    ''' name class '''
    first: str = ""
    last: str = ""
