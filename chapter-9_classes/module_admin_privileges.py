"""This module defines the Admin and Privileges classes.

The Admin class inherits from the User class, from `module_user` module,
and represents an administrator with specific privileges.

The Privileges class represents the privileges assigned to an administrator."""

import module_user


class Admin(module_user.User):
    """
    Admin class that inherits from the User class and represents an
    administrator with specific privileges.

    Attributes:

        privileges : list
            A list of privileges assigned to the admin.

    Methods:

        show_privileges(): Displays the administrator's privileges."""

    def __init__(self, first_name, last_name, nickname):
        """
        Initialize the Admin class with first name, last name, and nickname.

        Args:
            first_name (str): The first name of the admin.
            last_name (str): The last name of the admin.
            nickname (str): The nickname of the admin.
        """
        super().__init__(first_name, last_name, nickname)
        self.privileges = Privileges()


class Privileges:
    """
    A class to represent the privileges of an administrator.

    Attributes:

        privileges (list): A list of privileges assigned to the administrator.

    Methods:

        show_privileges():
            Display the administrator's privileges."""

    def __init__(self, privileges=["add post", "delete post", "ban user"]):
        """
        Initialize the Privileges class with a list of privileges.

        Args:
            privileges (list, optional): A list of privileges.
            Defaults to ["add post", "delete post", "ban user"].
        """
        self.privileges = privileges

    def show_privileges(self):
        """Display the administrator's privileges."""
        print(f"Administrator privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")
