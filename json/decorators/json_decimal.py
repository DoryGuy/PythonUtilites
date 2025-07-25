#
# pylint: disable=line-too-long
#
"""
# File Name:     json_decimal.py
# Programmer:    Gary Powell
# Date:          April 16, 2025
#
# Problem Statement: Custom encode and decode of Decimal
#
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
            return { '__Decimal__': True, 'value': str(obj) }
        if hasattr(obj, '__dict__'):
            return obj.__dict__       # happens to work for my use case.
        return super().default(obj)   # return the default JSONEncoder behavior

class JsonDecimalDecoder(JSONDecoder):
    """ convert JSON Decimal to Decimal """
    def __init__(self, *args, **kwargs):
        """ initialize the class """
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, data):  # pylint: disable=E0202
        """ override the object_hook member fn """
        if '__Decimal__' in data:
            return Decimal(data['value'])
        return data
