"""Make a class called User. Create two attributes called first_name and
last_name, and then create several other attributes that are typically
stored in a user profile. Make a method called describe_user() that prints
a summary of the user's information. Make another method called greet_user()
that prints a personalized greeting to the user. Create several instances
representing different users, and call both methods for each user."""


class User:
    """A class to represent a user.

    Attributes:
    ----------
    first_name : str
        The first name of the user
    last_name : str
        The last name of the user
    age : int
        The age of the user
    nickname : str
        The nickname of the user
    tribe : str
        The tribe of the user


    Methods
    ----------
        describe_user():
            Prints a formatted string that describes the user with their first name,
            last name, age, nickname, and tribe. The description includes special
            Unicode characters for visual enhancement.
        greet_user():
            Prints a greeting message to the user including their nickname. The
            greeting message includes a waving hand emoji and a welcome message"""

    def __init__(self, first_name, last_name, age, nickname, tribe):
        """Initialize a new user instance.

        Args:
            first_name (str): The first name of the user.
            last_name (str): The last name of the user.
            age (int): The age of the user.
            nickname (str): The nickname of the user.
            tribe (str): The tribe of the user.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nickname = nickname
        self.tribe = tribe

    def describe_user(self):
        """Prints a formatted string that describes the user
        with their first name, last name, age, nickname, and tribe.
        The description includes special Unicode characters for visual enhancement.
        """

        print(
            f"\n\U00002728 {self.first_name} {self.last_name}"
            f"\n\U00002666 Age: {self.age}"
            f"\n\U00002666 Nickname: {self.nickname}"
            f"\n\U00002666 Tribe: {self.tribe}"
        )

    def greet_user(self):
        """Prints a greeting message to the user including their nickname.
        The greeting message includes a waving hand emoji and a welcome message
        that addresses the user by their nickname.
        Returns:
            None
        """

        print(f"\U0001F44B Welcome, {self.first_name}! Ready for your next adventure?")


users = {
    "naruto": {
        "first_name": "Naruto",
        "last_name": "Uzumaki",
        "age": 17,
        "nickname": "The Seventh Hokage",
        "tribe": "Uzumaki Clan",
    },
    "sasuke": {
        "first_name": "Sasuke",
        "last_name": "Uchiha",
        "age": 17,
        "nickname": "The Avenger",
        "tribe": "Uchiha Clan",
    },
    "sakura": {
        "first_name": "Sakura",
        "last_name": "Haruno",
        "age": 17,
        "nickname": "The Cherry Blossom Medic",
        "tribe": "Team 7",
    },
    "kakashi": {
        "first_name": "Kakashi",
        "last_name": "Hatake",
        "age": 29,
        "nickname": "The Copy Ninja",
        "tribe": "Hatake Clan",
    },
    "hinata": {
        "first_name": "Hinata",
        "last_name": "Hyuga",
        "age": 17,
        "nickname": "The Gentle Fist",
        "tribe": "Hyuga Clan",
    },
    "shikamaru": {
        "first_name": "Shikamaru",
        "last_name": "Nara",
        "age": 17,
        "nickname": "The Shadow Strategist",
        "tribe": "Nara Clan",
    },
    "gaara": {
        "first_name": "Gaara",
        "last_name": "of the Sand",
        "age": 17,
        "nickname": "The Fifth Kazekage",
        "tribe": "Sand Village",
    },
    "itachi": {
        "first_name": "Itachi",
        "last_name": "Uchiha",
        "age": 21,
        "nickname": "The Fallen Hero",
        "tribe": "Uchiha Clan",
    },
    "jiraiya": {
        "first_name": "Jiraiya",
        "last_name": "of the Legendary Sannin",
        "age": 50,
        "nickname": "The Pervy Sage",
        "tribe": "Toad Sage",
    },
    "tsunade": {
        "first_name": "Tsunade",
        "last_name": "Senju",
        "age": 55,
        "nickname": "The Fifth Hokage",
        "tribe": "Senju Clan",
    },
}

for username, atributes in users.items():
    first_name = atributes["first_name"]
    last_name = atributes["last_name"]
    age = atributes["age"]
    nickname = atributes["nickname"]
    tribe = atributes["tribe"]
    user = User(first_name, last_name, age, nickname, tribe)
    user.describe_user()
    user.greet_user()
