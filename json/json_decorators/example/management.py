#
# pylint: disable=line-too-long,too-few-public-methods
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

from typing import Dict, Optional

from employee import Employee
from json_decorators import json_decorator
from json_encoders_decoders import MyJsonEncoder, MyJsonDecoder

@json_decorator(decoder=MyJsonDecoder, encoder=MyJsonEncoder, indent=4, sort_keys=True)
class EmployeeManagement:
    """ Hold all the employees """
    def __init__(self, *,next_employee_id:int = 1, employees: Optional[Dict[str, Employee]] = None) -> None:
        """ initialize the class """
        if employees is None:
            employees = {}
        self.next_employee_id = next_employee_id
        self.employees: Dict[str, Employee] = employees
