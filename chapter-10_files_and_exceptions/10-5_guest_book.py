"""Write a while loop that prompts users for their name.
Collect all the names that are entered, and then write these names to a file
called guest_book.txt. Make sure each entry appears on a new line in the file."""

from pathlib import Path

contents = ""
while True:
    user_name = input("What's your name? [Type 'q' to quit] ")
    if user_name.lower() != "q":
        contents += user_name
        contents += "\n"
    else:
        break

path = Path("chapter-10_files_and_exceptions/files/10-5_guest_book.txt")
path.write_text(contents)
