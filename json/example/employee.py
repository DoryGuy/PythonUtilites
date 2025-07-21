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
import json

from json_decimal import JsonDecimalEncoder, JsonDecimalDecoder

@dataclass(kw_only=True)
class Employee:
    """ Base Employee class """
    employee_id: str = ""
    first_name: str = ""
    last_name: str = ""
    pay_scale: Decimal = Decimal(0)

    def to_json(self) -> str:
        """ dump to json """
        return json.dumps(self,
                          sort_keys = True,
                          cls=JsonDecimalEncoder)

    def __eq__(self, other) -> bool:
        """ comparison of equality """
        return self.employee_id == other.employee_id

    def __hash__(self) -> int:
        """ use the employee id for the hash """
        return int(self.employee_id)

    def __ref__(self) -> str:
        """ return name of the class """
        return "Employee"

    @classmethod
    def from_json(cls, json_stuff):
        """ from a json dict """
        # pylint: disable=possibly-used-before-assignment
        if isinstance(json_stuff, str):
            data = json.loads(json_stuff, cls=JsonDecimalDecoder)
        elif isinstance(json_stuff, dict):
            data = json_stuff
        return cls(**data)

@dataclass(kw_only=True)
class PartTimeFaculty(Employee):
    """ Part time faculty """

    def to_json(self) -> str:
        """ dump to json """
        return json.dumps(self,
                          sort_keys = True,
                          cls=JsonDecimalEncoder)

    def __ref__(self) -> str:
        """ return name of the class """
        return "PartTimeFaculty"

    @classmethod
    def from_json(cls, json_stuff):
        """ create a PartTimeFaculty from json """
        # pylint: disable=possibly-used-before-assignment
        if isinstance(json_stuff, str):
            data = json.loads(json_stuff, cls=JsonDecimalDecoder)
        elif isinstance(json_stuff, dict):
            data = json_stuff
        return cls(**data)

@dataclass(kw_only=True)
class SalaryEmployee(Employee):
    """ Salary Employee """

    def to_json(self) -> str:
        """ dump to json """
        return json.dumps(self,
                          sort_keys = True,
                          cls=JsonDecimalEncoder)

    def __ref__(self) -> str:
        """ return name of the class """
        return "SalaryEmployee"

    @classmethod
    def from_json(cls, json_stuff):
        """ from a SalaryEmployee from json """
        # pylint: disable=possibly-used-before-assignment
        if isinstance(json_stuff, str):
            data = json.loads(json_stuff, cls=JsonDecimalDecoder)
        elif isinstance(json_stuff, dict):
            data = json_stuff
        return cls(**data)


@dataclass(kw_only=True)
class HourlyEmployee(Employee):
    """ Hourly Employee """

    def to_json(self) -> str:
        """ dump to json """
        return json.dumps(self,
                          sort_keys = True,
                          cls=JsonDecimalEncoder)

    def __ref__(self) -> str:
        """ return name of the class """
        return "HourlyEmployee"

    @classmethod
    def from_json(cls, json_stuff):
        """ create a Hourly Employee from a json"""
        # pylint: disable=possibly-used-before-assignment
        if isinstance(json_stuff, str):
            data = json.loads(json_stuff, cls=JsonDecimalDecoder)
        elif isinstance(json_stuff, dict):
            data = json_stuff
        return cls(**data)
