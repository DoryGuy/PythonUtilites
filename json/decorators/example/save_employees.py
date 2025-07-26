#
# pylint: disable=line-too-long
#
"""
# File Name:     save_employees.py
# Programmer:    Gary Powell
# Date:          May 19, 2025
#
# Problem Statement: Read and write the employee data
#
#
# Overall Plan:
#  Use a common format, ie JSON to store the data. It's not secure, but it allows
#  other programs to access the employee data.
"""

import json

from json_encoders_decoders import MyJsonEncoder
from management import EmployeeManagement

def save_employees(employees: EmployeeManagement) -> None:
    """ save the data in the employee management system """
    with open("employees/" + "employees.json", "w", encoding="utf-8") as emp_file:
        json.dump(employees, emp_file, sort_keys=True, indent=4, cls=MyJsonEncoder)

def get_employees() -> EmployeeManagement:
    """ read in the employee data """
    employee_mgt: EmployeeManagement = EmployeeManagement()
    try:
        with open("employees/" + "employees.json", "r", encoding="utf-8") as emp_file:
            return EmployeeManagement.from_json(emp_file.read())
    except FileNotFoundError:
        pass

    return employee_mgt
