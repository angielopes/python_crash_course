"""
This module provides a FileReader class to handle reading multiple files specified by the user.

Classes:
    FileReader: A class to handle reading multiple files specified by the user.
Usage Example:
    file_reader = FileReader()
    file_reader.add_files()
    contents = file_reader.read_files()
    print(contents)
"""

from pathlib import Path
from module_file_reader import FileReader


class FileReader:
    """
    A class to handle reading multiple files specified by the user.

    Methods:
        __init__():
            Initializes the FileReader instance with an empty list of file paths.
        add_files():
            Continuously prompts until the user enters 'q' to quit.
            Returns a list of file paths entered by the user.
        read_files():
            Reads the contents of files specified in the file_paths attribute.
            Returns a dictionary where the keys are file paths and the values are
            the contents of the corresponding files.
            Prints an error message if a file is not found."""

    def __init__(self):
        """
        Initialize the instance with an empty list of file paths.

        Attributes:
            file_paths (list): A list to store file paths.
        """
        self.file_paths = []

    def add_files(self):
        """
        Prompts the user to enter file paths and adds them to the file_paths attribute.
        This method continuously prompts the user to enter the path of a file until the user
        enters 'q' to quit. Each valid file path entered by the user is appended to the
        file_paths attribute of the instance.
        Returns:
            list: A list of file paths entered by the user.
        """
        while True:
            file_path = input("Enter the path of the file [or 'q' to quit]: ")
            if file_path.lower() == "q":
                break
            else:
                self.file_paths.append(file_path)
        return self.file_paths

    def read_files(self):
        """
        Reads the contents of files specified in the instance's file_paths attribute.
        This method iterates over the list of file paths stored in the instance's
        file_paths attribute, reads the content of each file, and stores the content
        in a dictionary with the file path as the key. If a file is not found, it
        prints an error message indicating the missing file.
        Returns:
            dict: A dictionary where the keys are file paths and the values are the
                  contents of the corresponding files.
        """

        file_contents = {}
        for file_path in self.file_paths:
            try:
                path_object = Path(file_path)
                content = path_object.read_text(encoding="utf-8")
                file_contents[file_path] = content
                print(f"File '{file_path}' read successfully.")
            except FileNotFoundError:
                print(f"The file {file_path} does not exist.")
        return file_contents
