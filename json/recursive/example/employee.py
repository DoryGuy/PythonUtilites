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
import json

from json_decimal import JsonDecimalEncoder, JsonDecimalDecoder
from json_convert import convert_to_json
from name import Name

@dataclass(kw_only=True)
class Employee:
    """ Base Employee class """
    employee_id: str = ""
    name: Name = field(default_factory=lambda: Name())
    pay_scale: Decimal = Decimal(0)

    def to_json(self) -> str:
        """ dump to json """
        return json.dumps(convert_to_json(self),
                          sort_keys = True,
                          indent = 4,
                          cls=JsonDecimalEncoder)

    def __eq__(self, other) -> bool:
        """ comparison of equality """
        return self.employee_id == other.employee_id

    def __hash__(self) -> int:
        """ use the employee id for the hash """
        return int(self.employee_id)

    @classmethod
    def from_json(cls, json_stuff):
        """ from a json dict """
        # pylint: disable=possibly-used-before-assignment
        if isinstance(json_stuff, (bytes, bytearray, str)):
            data = json.loads(json_stuff, cls=JsonDecimalDecoder)
        elif isinstance(json_stuff, dict):
            data = json_stuff
        return cls(**data)

@dataclass(kw_only=True)
class PartTimeFaculty(Employee):
    """ Part time faculty """

    def to_json(self) -> str:
        """ dump to json """
        return json.dumps(convert_to_json(self),
                          sort_keys = True,
                          indent = 4,
                          cls=JsonDecimalEncoder)

    @classmethod
    def from_json(cls, json_stuff):
        """ create a PartTimeFaculty from json """
        # pylint: disable=possibly-used-before-assignment
        if isinstance(json_stuff, (bytes, bytearray, str)):
            data = json.loads(json_stuff, cls=JsonDecimalDecoder)
        elif isinstance(json_stuff, dict):
            data = json_stuff
        return cls(**data)

@dataclass(kw_only=True)
class SalaryEmployee(Employee):
    """ Salary Employee """

    def to_json(self) -> str:
        """ dump to json """
        return json.dumps(convert_to_json(self),
                          sort_keys = True,
                          indent = 4,
                          cls=JsonDecimalEncoder)

    @classmethod
    def from_json(cls, json_stuff):
        """ from a SalaryEmployee from json """
        # pylint: disable=possibly-used-before-assignment
        if isinstance(json_stuff, (bytes, bytearray, str)):
            data = json.loads(json_stuff, cls=JsonDecimalDecoder)
        elif isinstance(json_stuff, dict):
            data = json_stuff
        return cls(**data)


@dataclass(kw_only=True)
class HourlyEmployee(Employee):
    """ Hourly Employee """

    def to_json(self) -> str:
        """ dump to json """
        return json.dumps(convert_to_json(self),
                          sort_keys = True,
                          indent = 4,
                          cls=JsonDecimalEncoder)

    @classmethod
    def from_json(cls, json_stuff):
        """ create a Hourly Employee from a json"""
        # pylint: disable=possibly-used-before-assignment
        if isinstance(json_stuff, (bytes, bytearray, str)):
            data = json.loads(json_stuff, cls=JsonDecimalDecoder)
        elif isinstance(json_stuff, dict):
            data = json_stuff
        return cls(**data)
