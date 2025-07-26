#
# pylint: disable=line-too-long
#
"""
# File Name:     main.py
# Programmer:    Gary Powell
# Date:          May 16, 2025
#
#
# Overall Plan:
"""

from save_employees import get_employees, save_employees

def main() -> None:
    """ main """
    employee_mgt = get_employees()
    save_employees(employee_mgt)

    print("Done!")

# This code runs only when the module is executed directly.
if __name__ == '__main__':
    main()
