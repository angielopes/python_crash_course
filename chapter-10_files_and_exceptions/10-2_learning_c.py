"""You can use the replace() method to replace any word in a string with a
different word. Here's a quick example showing how to replace 'dog' with 'cat' in a sentence.
Read in each line from the file you just created, learning_python.txt, and
replace the word Python with the name of another language, such as C.
Print each modified line to the screen."""

from pathlib import Path

path = Path("chapter-10_files_and_exceptions/files/10-1_learning_c.txt")
contents = path.read_text().replace("Python", "C")

file_string = ""
for content in contents:
    file_string += content

print(file_string)
