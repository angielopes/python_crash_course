class Employee:
    """
    A class to represent an employee.

    Attributes
    ----------
    first_name : str
        The first name of the employee.
    last_name : str
        The last name of the employee.
    annual_salary : float
        The annual salary of the employee.

    Methods
    -------
    give_raise(rise=5000) -> int:
        Adds the specified amount to the employee's annual salary.
    """

    def __init__(self, first_name: str, last_name: str, annual_salary: float) -> None:
        """
        Initialize an Employee object.

        Args:
            first_name (str): The first name of the employee.
            last_name (str): The last name of the employee.
            annual_salary (float): The annual salary of the employee.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, rise=5000) -> int:
        """
        Add a specified amount to the employee's annual salary.

        Args:
            rise (int, optional): The amount to add to the annual salary. Defaults to 5000.
        Returns:
            int: The updated annual salary.
        """
        self.annual_salary += rise
