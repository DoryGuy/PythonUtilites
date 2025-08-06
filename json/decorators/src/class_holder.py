# pylint: disable=line-too-long
'''
json decorator class to hold a list of json class names for decoding.
'''

class ClassHolder:
    '''
    https://stackoverflow.com/questions/1176136/convert-string-to-python-class-object
    '''

    def __init__(self):
        ''' init '''
        self.classes = {}

    # -- the decorator
    def register(self, c):
        ''' register a class with the holder '''
        self.classes[c.__name__] = c

        # Decorators have to return the function/class passed (or a modified variant thereof)
        return c

    def __getitem__(self, n):
        ''' get a class by name '''
        return self.classes[n]
