#
# pylint: disable=line-too-long
#
"""
# Programmer:    Gary Powell
# Date:          April 16, 2025
#
# Problem Statement: Customer encode and decode of Decimal
#
# Overall Plan:
    Custom decoder to read and write Decimal values
"""

from decimal import Decimal
from json import JSONDecoder, JSONEncoder

class JsonDecimalEncoder(JSONEncoder):
    """ convert Decimal to JSON Decimal """
    def default(self, obj):         # pylint: disable=arguments-renamed
        """ override the default """
        if isinstance(obj, Decimal):
            return { '__Decimal__': str(obj) }
        if hasattr(obj, '__dict__'):
            return obj.__dict__
        return super().default(obj)

class JsonDecimalDecoder(JSONDecoder):
    """ convert JSON Decimal to Decimal """
    def __init__(self, *args, **kwargs):
        """ initialize the class """
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, obj):  # pylint: disable=E0202
        """ override the object_hook member fn """
        if '__Decimal__' in obj:
            return Decimal(obj['__Decimal__'])
        return obj
