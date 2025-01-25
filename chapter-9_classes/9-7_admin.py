"""An administrator is a special kind of user.
Write a class called Admin that inherits from the User class you wrote in
Exercise 9-3 (page 162) or Exercise 9-5 (page 167). Add an attribute,
privileges, that stores a list of strings like "can add post",
"can delete post", "can ban user", and so on. Write a method called
show_privileges() that lists the administrator's set of privileges.
Create an instance of Admin, and call your method."""


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


class Admin(User):
    """Admin class that inherits from the User class
    and represents an administrator with specific privileges.

    Attributes:
    ----------
        privileges : list
            A list of privileges assigned to the admin.

    Methods:
    ----------
        show_privileges(): Displays the administrator's privileges."""

    def __init__(self, first_name, last_name, nickname):
        """Initialize the Admin class with first name, last name, and nickname.

        Args:
            first_name (str): The first name of the admin.
            last_name (str): The last name of the admin.
            nickname (str): The nickname of the admin.
        """

        super().__init__(first_name, last_name, nickname)
        self.privileges = ["add post", "delete post", "ban user"]

    def show_priveleges(self):
        """Display the administrator's privileges."""

        print(f"Administrator privileges:")
        print(f"{self.privileges}")


administrator_1 = Admin("Marceline", "da Silva", "marcelinha")
administrator_1.describe_user()
administrator_1.show_priveleges()
