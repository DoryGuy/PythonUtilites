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
from employee import HourlyEmployee, SalaryEmployee, PartTimeFaculty, Employee

class JsonEmployeeEncoder(json.JSONEncoder):
    """ convert employee classes to JSON """

    def default(self,obj):      # pylint: disable=arguments-renamed
        """ override the default """
        if isinstance(obj, Employee):
            if hasattr(obj, 'to_json') and callable(getattr(obj, 'to_json')):
                return { "__" + obj.__class__.__name__ + "__": True, 'value': obj.to_json() }
        return obj.__dict__

class JsonEmployeeDecoder(json.JSONDecoder):
    """ convert JSON to Employee classes """

    def __init__(self, *args, **kwargs):
        """ initialize the class """
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, data):  # pylint: disable=E0202
        """ override the object_hook member fn """
        if '__PartTimeFaculty__' in data:
            return PartTimeFaculty.from_json(data['value'])
        if '__SalaryEmployee__' in data:
            return SalaryEmployee.from_json(data['value'])
        if '__HourlyEmployee__' in data:
            return HourlyEmployee.from_json(data['value'])
        return data
