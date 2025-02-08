"""Write a program that prompts for the user's favorite number.
Use json.dumps() to store this number in a file. Write a separate program
that reads in this value and prints the message:
'I know your favorite number! It's _____.'"""

from pathlib import Path
import json


def get_favorite_number():
    """
    Prompts the user to input their favorite number, validates the input,
    and saves it to a JSON file.
    The function repeatedly asks the user for their favorite number until
    a valid integer is provided. The valid number is then saved to a file
    named 'favorite_number.json' located in the 'chapter-10_files_and_exceptions/files/'
    directory.
    Returns:
        int: The user's favorite number.
    """

    while True:
        try:
            fav_number = int(input("What's your favorite number? "))
            if int(fav_number):
                break
            else:
                print("It needs to be an integer.")
        except ValueError:
            print("It needs to be an integer.")

    path = Path("chapter-10_files_and_exceptions/files/favorite_number.json")
    contents = json.dumps(fav_number)
    path.write_text(contents)
    return fav_number


def read_favorite_number():
    """
    Reads and prints the user's favorite number.
    This function attempts to retrieve the user's favorite number by calling
    the `get_favorite_number` function. If a favorite number is found, it
    prints a message indicating the favorite number. If no favorite number
    is found, it calls `get_favorite_number` again and prints a message
    indicating that the favorite number is now known.
    """

    number = get_favorite_number()
    if number:
        print(f"I know your favorite number! It's {number}")
    else:
        number = get_favorite_number()
        print(f"Now I now your favorite number :)")


read_favorite_number()
