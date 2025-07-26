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

    def add_class(self, c):
        ''' add a class to the holder '''
        self.classes[c.__name__] = c

    # -- the decorator
    def register(self, c):
        ''' register a class with the holder '''
        self.add_class(c)

        # Decorators have to return the function/class passed (or a modified variant thereof), however I'd rather do this separately than retroactively change add_class, so.
        # "held" is more succint, anyway.
        return c

    def __getitem__(self, n):
        ''' get a class by name '''
        return self.classes[n]
