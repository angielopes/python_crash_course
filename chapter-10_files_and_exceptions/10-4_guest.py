"""Write a program that prompts the user for their name.
When they respond, write their name to a file called guest.txt."""

from pathlib import Path

user_name = input("What's your name? ")

path = Path("chapter-10_files_and_exceptions/files/10-4_guest.txt")
path.write_text(user_name)
