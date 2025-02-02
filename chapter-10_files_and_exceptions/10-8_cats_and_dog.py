"""Make two files, cats.txt and dogs.txt. Store at least three names of cats
in the first file and three names of dogs in the second file.
Write a program that tries to read these files and print the contents of the
file to the screen. Wrap your code in a try-except block to catch the
FileNotFound error, and print a friendly message if a file is missing.
Move one of the files to a different location on your system, and make sure
the code in the except block executes properly."""

from pathlib import Path

# file_path = Path("chapter-10_files_and_exceptions/files/cats.txt")
# file_path.write_text(
#     "Lolita\nBambu\nFrodo\nFrida\nFaísca\nTapioca\nJennie\nMarceline\nNaniquinha\nMonCherri\nStacy",
#     encoding="utf-8",
# )

# file_path = Path("chapter-10_files_and_exceptions/files/dogs.txt")
# file_path.write_text(
#     "Dick Bob\nCarolino\nJujuba\nLupita",
#     encoding="utf-8",
# )


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
        print(f"\nSorry, the file {file_path} does not exist.")
    else:
        print(f"\n{file_path} content:")
        print(f"{file_contents}")
