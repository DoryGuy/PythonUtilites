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
from json_employee import JsonEmployeeEncoder, JsonEmployeeDecoder

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
                          cls=JsonEmployeeEncoder)

    def __str__(self) -> str:
        """ class name """
        return "EmployeeManagement"

    def __ref__(self) -> str:
        """ class name """
        return "EmployeeManagement"

    @classmethod
    def from_json(cls, stuff):
        """ from a json dict """
        return cls(**stuff, cls=JsonEmployeeDecoder)
