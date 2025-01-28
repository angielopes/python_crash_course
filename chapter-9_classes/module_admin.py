"""This module defines classes for managing users and administrators with specific privileges.

Classes:
    User: Represents a user with login attempt tracking.
    Admin: Inherits from User and represents an administrator with specific privileges.
    Privileges: Represents the privileges assigned to an administrator."""


class User:
    """
    A class to represent a user with login attempt tracking.

    Attributes:

    first_name : str
        The first name of the user
    last_name : str
        The last name of the user
    nickname : str
        Nickname of the user
    login_attempts : int
        Loging attempts made by the user

    Methods:

        describe_user(): Prints a summary of the user's information.
        increment_login_attempts(logins): Increment the number of login attempts by a specified amount.
        reset_login_attempts(): Reset the number of login attempts to zero and prints a message about it.
    """

    def __init__(self, first_name, last_name, nickname):
        """
        Initialize a new User instance.

        Args
            first_name (str): The user's first name.
            last_name (str): The user's last name.
            nickname (str): The user's nickname.

        Attributes
            first_name (str): The user's first name.
            last_name (str): The user's last name.
            nickname (str): The user's nickname.
            login_attempts (int): The number of login attempts made by the user, initialized to 0.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname
        self.login_attempts = 0

    def describe_user(self):
        """
        Prints a summary of the user's information, including their first name, last name,
        nickname, and the number of login attempts.
        """
        print(
            f"{self.first_name} {self.last_name}"
            f"\nNickname: {self.nickname}"
            f"\nLogin attempts: {self.login_attempts}"
        )

    def increment_login_attempts(self, logins):
        """
        Increment the number of login attempts by a specified amount.

        Args:
            logins (int): The number of login attempts to add to the current count.
        """
        self.login_attempts += logins

    def reset_login_attempts(self):
        """
        Reset the number of login attempts to zero and prints a message about it."""
        self.login_attempts = 0
        print("\nResetting the login attempts...")


class Admin(User):
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
