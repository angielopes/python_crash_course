"""You can use the replace() method to replace any word in a string with a
different word. Here's a quick example showing how to replace 'dog' with 'cat' in a sentence.
Read in each line from the file you just created, learning_python.txt, and
replace the word Python with the name of another language, such as C.
Print each modified line to the screen."""

from pathlib import Path

path = Path("chapter-10_files_and_exceptions/files/10-1_learning_c.txt")
contents = path.read_text()

lines = contents.replace("Python", "C")  # Makes a copy
file_string = ""
for line in lines:
    file_string += line


print(file_string)
print("\n")
print(contents)
