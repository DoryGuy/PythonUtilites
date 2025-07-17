#
# pylint: disable=line-too-long
#
"""
# File: json_employee.py
# Programmer: Gary Powell
# Date: May 21, 2025
#
# Problem Statement: Classes write Employee data in Json
#
# Overall Plan:
#   Use as much of the json library as possible.
"""

import json
from employee import HourlyEmployee, PartTimeFaculty, SalaryEmployee
from json_decimal import JsonDecimalDecoder

class JsonEmployeeEncoder(json.JSONEncoder):
    """ convert employee classes to JSON """

    def default(self,obj):      # pylint: disable=arguments-renamed
        """ override the default """
        if isinstance(obj, PartTimeFaculty):
            return { '__PartTimeFaculty__': True, 'value': obj.to_json() }
        if isinstance(obj, SalaryEmployee):
            return { '__SalaryEmployee__': True, 'value': obj.to_json() }
        if isinstance(obj, HourlyEmployee):
            return { '__HourlyEmployee__': True, 'value': obj.to_json() }
        return obj.__dict__

class JsonEmployeeDecoder(json.JSONDecoder):
    """ convert JSON to Employees """

    def __init__(self, *args, **kwargs):
        """ initialize the class """
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, data):  # pylint: disable=E0202
        """ override the object_hook member fn """
        if '__PartTimeFaculty__' in data:
            v = json.loads(data['value'], cls=JsonDecimalDecoder)
            return PartTimeFaculty(**v)
        if '__SalaryEmployee__' in data:
            v = json.loads(data['value'], cls=JsonDecimalDecoder)
            return SalaryEmployee(**v)
        if '__HourlyEmployee__' in data:
            v = json.loads(data['value'], cls=JsonDecimalDecoder)
            return HourlyEmployee(**v)
        return data
