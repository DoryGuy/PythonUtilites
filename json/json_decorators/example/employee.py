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
from dataclasses import dataclass
from decimal import Decimal

from json_decorators import json_decorator
from json_encoders_decoders import MyJsonEncoder, MyJsonDecoder
from json_register import json_class_registry

@dataclass(kw_only=True)
@json_decorator(encoder=MyJsonEncoder,decoder=MyJsonDecoder)
class Employee:
    """ Base Employee class """
    employee_id: str
    first_name: str
    last_name: str
    pay_scale: Decimal

    def __eq__(self, other) -> bool:
        """ comparison of equality """
        return self.employee_id == other.employee_id

    def __hash__(self) -> int:
        """ use the employee id for the hash """
        return int(self.employee_id)


@dataclass(kw_only=True)
@json_class_registry.register
@json_decorator(encoder=MyJsonEncoder,decoder=MyJsonDecoder)
class PartTimeFaculty(Employee):
    """ Part time faculty """


@dataclass(kw_only=True)
@json_class_registry.register
@json_decorator(encoder=MyJsonEncoder,decoder=MyJsonDecoder)
class SalaryEmployee(Employee):
    """ Salary Employee """

@dataclass(kw_only=True)
@json_class_registry.register
@json_decorator(encoder=MyJsonEncoder,decoder=MyJsonDecoder)
class HourlyEmployee(Employee):
    """ Hourly Employee """
