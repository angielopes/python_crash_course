"""Add an attribute called login_attempts to your User class from Exercise 9-3
(page 162). Write a method called increment_login_attempts() that increments
the value of login_attempts by 1. Write another method called
reset_login_attempts() that resets the value of login_attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was
incremented properly, and then call reset_login_attempts().
Print login_attempts again to make sure it was reset to 0."""


class User:
    """A class to represent a user with login attempt tracking.

    Attributes:
    ----------
    first_name : str
        The first name of the user
    last_name : str
        The last name of the user
    nickname : str
        Nickname of the user
    login_attempts : int
        Loging attempts made by the user

    Methods:
    ----------
        describe_user(): Prints a summary of the user's information.
        increment_login_attempts(logins): Increment the number of login attempts by a specified amount.
        reset_login_attempts(): Reset the number of login attempts to zero and prints a message about it.
    """

    def __init__(self, first_name, last_name, nickname):
        """Initialize a new User instance.

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
        """Prints a summary of the user's information,
        including their first name, last name,
        nickname, and the number of login attempts.
        """
        print(
            f"{self.first_name} {self.last_name}"
            f"\nNickname: {self.nickname}"
            f"\nLogin attempts: {self.login_attempts}"
        )

    def increment_login_attempts(self, logins):
        """Increment the number of login attempts by a specified amount.

        Args:
            logins (int): The number of login attempts to add to the current count.
        """
        self.login_attempts += logins

    def reset_login_attempts(self):
        """Reset the number of login attempts to zero
        and prints a message about it."""
        self.login_attempts = 0
        print("\nResetting the login attempts...")


user_1 = User("Angela", "Lopes", "angiekill")
user_1.increment_login_attempts(5)
user_1.increment_login_attempts(6)
user_1.increment_login_attempts(7)
user_1.increment_login_attempts(8)
user_1.describe_user()
user_1.reset_login_attempts()
user_1.describe_user()
