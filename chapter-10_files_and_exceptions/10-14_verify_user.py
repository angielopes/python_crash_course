"""The final listing for remember_me.py assumes either that the user has
already entered their username or that the program is running for the
first time. We should modify it in case the current user is not the person
who last used the program. Before printing a welcome back message
in greet_user(), ask the user if this is the correct username.
If it's not, call get_new_username() to get the correct username."""

from pathlib import Path
import json


def get_stored_user_info(path):
    """
    Retrieve stored user information  from a given file path.
    Args:
            path (Path): The file path to the user information file.
    Returns:
            dict or None: A dictionary containing user information if the file exists,
                      otherwise None.
    """
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None


def get_new_user_info(path):
    """
    Prompt the user for their full name, age, and username, then save this information to a file.
    Args:
        path (Path): The file path where the user information will be saved.
    Returns:
        dict: A dictionary containing the user's full name, age, and username.
    """
    user_info = {}

    user_info["username"] = input("Type your username: ")
    user_info["full_name"] = input("What's your full name? ")

    while True:
        try:
            user_info["age"] = int(input("Your age: "))
            break
        except ValueError:
            print("It needs to be an integer.")

    contents = json.dumps(user_info)
    path.write_text(contents)

    return user_info


def greet_user():
    """
    Greet the user and verify their information.
    This function retrieves stored user information from a JSON file and
    prompts the user to confirm if the information is correct.
    If the information is correct, it displays the user's summary.
    If not, it prompts the user to enter new information and saves it.

    Parameters:
                None
    Returns:
                None
    """

    path = Path("chapter-10_files_and_exceptions/files/user_info.json")
    user_info = get_stored_user_info(path)

    print(f"Username: {user_info['username']}")

    confirm = input(
        f"Is the username {user_info['username']} corret? Type 'y' for YES or 'n' for NO: "
    )

    if confirm.lower() == "y":
        print("\nWelcome back!")
        print(f"Full name: {user_info['full_name']}")
        print(f"Age: {user_info['age']}")
        print(f"Username: {user_info['username']}")

    else:
        print("\nPlease, informe your user details")
        user_info = get_new_user_info(path)
        print("Thank you! Your information has been saved!")


greet_user()
