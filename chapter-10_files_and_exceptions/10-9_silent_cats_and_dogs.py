"""Modify your except block in Exercise 10-7 to fail silently if either file is missing."""

from pathlib import Path

file_paths = [
    "chapter-10_files_and_exceptions/files/cats.txt",
    "no_path_in_here.txt",
    "chapter-10_files_and_exceptions/files/dogs.txt",
]

for file_path in file_paths:
    try:
        file_read = Path(file_path)
        file_contents = file_read.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass
    else:
        print(f"{file_path} content:")
        print(f"\n{file_contents}")
