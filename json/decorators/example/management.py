#
# pylint: disable=line-too-long
#
"""
# Exercise No.   Hw12 Project 1
# File Name:     hw10GetPositiveInteger.py
# Programmer:    Gary Powell
# Date:          April 14, 2025
#
# Problem Statement: Classes to hold a management tool.
#
# Overall Plan:
"""

import json
from typing import Dict, Optional

from employee import Employee
from json_encoders_decoders import MyJsonEncoder, MyJsonDecoder

class EmployeeManagement:
    """ Hold all the employees """
    def __init__(self, *,next_employee_id:int = 1, employees: Optional[Dict[str, Employee]] = None) -> None: #
        """ initialize the class """
        if employees is None:
            employees = {}
        self.next_employee_id = next_employee_id
        self.employees: Dict[str, Employee] = employees

    def to_json(self) -> str:
        """ dump to json """
        return json.dumps(self,
                          sort_keys = True,
                          indent=4,
                          cls=MyJsonEncoder)

    @classmethod
    def from_json(cls, json_stuff):
        """ from a json dict """
        # pylint: disable=possibly-used-before-assignment
        if isinstance(json_stuff, (bytes, bytearray, str)):
            data = json.loads(json_stuff, cls=MyJsonDecoder)
        elif isinstance(json_stuff, dict):
            data = json_stuff
        return cls(**data)
