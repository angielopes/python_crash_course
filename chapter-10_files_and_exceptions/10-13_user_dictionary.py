"""The remember_me.py example only stores one piece of information, the username.
Expand this example by asking for two more pieces of information about the user,
then store all the information you collect in a dictionary. Write this dictionary
to a file using json.dumps(), and read it back in using json.loads().
Print a summary showing exactly what your program remembers about the user."""

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
    # docstring
    user_info = {}
    user_info["full_name"] = input("What's your full name? ")

    while True:
        try:
            user_info["age"] = int(input("Your age: "))
            break
        except ValueError:
            print("It needs to be an integer.")

    user_info["username"] = input("Type your user name: ")

    contents = json.dumps(user_info)
    path.write_text(contents)

    return user_info


def greet_user():

    path = Path("chapter-10_files_and_exceptions/files/user_info.json")
    user_info = get_stored_user_info(path)

    if user_info:
        print("USER SUMMARY")
        print(f"Full name: {user_info["full_name"]}")
        print(f"Age: {user_info["age"]}")
        print(f"Username: {user_info["username"]}")
    else:
        print("Please, informe your user details")
        user_info = get_new_user_info(path)
        print("Thank you! Your information has been saved!")


greet_user()
