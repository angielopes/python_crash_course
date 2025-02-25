"""
This module contains unit tests for the Employee class using pytest.

Fixtures:
    employee_salary: A pytest fixture that creates an Employee instance with a default salary.

Test Functions:
    test_give_default_raise(employee_salary): Tests the give_raise method with the default raise amount.
    test_give_custom_raise(employee_salary): Tests the give_raise method with a custom raise amount.
"""

import pytest
from module_employee import Employee


@pytest.fixture
def employee_salary():
    """
    Create an Employee instance with predefined attributes.
    This function creates an Employee object with the first name "Angela",
    last name "Lopes", and a salary of 10,000.

    Returns:
        Employee: An instance of the Employee class with the specified attributes.
    """
    employee_salary = Employee("Angela", "Lopes", 10_000)
    return employee_salary


def test_give_default_raise(employee_salary):
    """
    Test the give_raise method with the default raise amount.
    This test checks if the give_raise method correctly updates the
    employee's annual salary when no specific raise amount is provided.

    Args:
        employee_salary (Employee): An instance of the Employee class
        with an initial annual salary of 10,000.

    Asserts:
        The employee's annual salary should be updated to 15,000 after
        the default raise is applied.
    """
    employee_salary.give_raise()
    assert employee_salary.annual_salary == 15_000


def test_give_custom_raise(employee_salary):
    """
    Test the give_raise method of the Employee class with a custom raise amount.
    This test checks if the annual salary of the employee is correctly updated
    when a custom raise amount of 3,000 is given.

    Args:
        employee_salary (Employee): An instance of the Employee class with an initial salary.

    Asserts:
        The annual salary of the employee should be 13,000 after the raise.
    """
    employee_salary.give_raise(3_000)
    assert employee_salary.annual_salary == 13_000
