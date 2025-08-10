#
# pylint: disable=line-too-long
#
"""
# File: employee.py
# Programmer: Gary Powell
# Date: May 12, 2025
#
# Problem Statement: Classes to hold employee data
#
# Overall Plan:
#    Create a base class to hold common employee data.
#    Create a class for Part time, Salary, and hourly
#    employees.
"""
from dataclasses import dataclass, field
from decimal import Decimal
from typing import List

from address import Address
from contacts import Contact
from json_decorators import json_decorator
from json_encoders_decoders import MyJsonEncoder, MyJsonDecoder
from json_register import json_class_registry
from name import Name

@dataclass(kw_only=True)
class Employee:
    """ Base Employee class """
    #pylint: disable=unnecessary-lambda
    address: Address = field(default_factory=lambda: Address())
    contacts: List[Contact]
    employee_id: str
    name: Name = field(default_factory=lambda: Name())
    pay_scale: Decimal

    def __eq__(self, other) -> bool:
        """ comparison of equality """
        return self.employee_id == other.employee_id

    def __hash__(self) -> int:
        """ use the employee id for the hash """
        return int(self.employee_id)

@dataclass(kw_only=True)
@json_class_registry.register
@json_decorator(encoder=MyJsonEncoder, decoder=MyJsonDecoder, indent=4, sort_keys=True)
class PartTimeFaculty(Employee):
    """ Part time faculty """

@dataclass(kw_only=True)
@json_class_registry.register
@json_decorator(encoder=MyJsonEncoder, decoder=MyJsonDecoder, indent=4, sort_keys=True)
class SalaryEmployee(Employee):
    """ Salary Employee """


@dataclass(kw_only=True)
@json_class_registry.register
@json_decorator(encoder=MyJsonEncoder, decoder=MyJsonDecoder, indent=4, sort_keys=True)
class HourlyEmployee(Employee):
    """ Hourly Employee """
