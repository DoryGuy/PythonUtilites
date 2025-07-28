#
# pylint: disable=line-too-long
#
"""
# Programmer: Gary Powell
# Date: May 21, 2025
#
# Problem Statement: Classes write Employee data in Json
#
# Overall Plan:
#   Use as much of the json library as possible.
"""

import json
from employee import HourlyEmployee, SalaryEmployee, PartTimeFaculty, Employee

class MyJsonEncoder(json.JSONEncoder):
    """ convert employee classes to JSON """

    def default(self,obj):      # pylint: disable=arguments-renamed
        """ override the default """
        if isinstance(obj, Employee):
            if hasattr(obj, 'to_json') and callable(getattr(obj, 'to_json')):
                return { "__" + obj.__class__.__name__ + "__": obj.to_json() }
        if hasattr(obj, '__dict__'):
            # If the object has a __dict__ attribute, return it
            return obj.__dict__
        return super().default(obj)  # Call the default method of the parent class

class MyJsonDecoder(json.JSONDecoder):
    """ convert JSON to Employee classes """

    def __init__(self, *args, **kwargs):
        """ initialize the class """
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, obj):  # pylint: disable=E0202
        """ override the object_hook member fn """
        if '__PartTimeFaculty__' in obj:
            return PartTimeFaculty.from_json(obj['__PartTimeFaculty__'])
        if '__SalaryEmployee__' in obj:
            return SalaryEmployee.from_json(obj['__SalaryEmployee__'])
        if '__HourlyEmployee__' in obj:
            return HourlyEmployee.from_json(obj['__HourlyEmployee__'])
        return obj
