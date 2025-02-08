"""
This module provides a FileReader class for reading the contents of multiple files.

Classes:
    FileReader: A class to manage file paths and read their contents.

Usage Example:
    file_reader = FileReader()
    file_reader.add_files()
    file_reader.read_files()
"""

from pathlib import Path


class FileReader:
    """
    A class to handle reading multiple files.

    Attributes:
    -----------

    file_paths : list
        A list to store file paths added by the user.

    Methods:
    --------

    add_files():
        Prompts the user to input file paths and adds them to the file_paths list.
        Returns the list of file paths.
    read_files():
        Reads the content of each file in the file_paths list.
        Prints an error message if a file is not found.
    """

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
        Reads the content of files specified in the file_paths attribute.
        Iterates over each file path in the file_paths attribute, attempts to read
        the content of each file using UTF-8 encoding, and stores the content in a
        variable. If a file is not found, it prints an error message indicating
        that the file does not exist.
        Raises:
            FileNotFoundError: If a file specified in file_paths does not exist.
        Returns:
            None
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
