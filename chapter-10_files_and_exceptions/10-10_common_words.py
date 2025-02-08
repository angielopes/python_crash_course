"""Visit Project Gutenberg (https://gutenberg.org ) and find a few texts you'd
like to analyze. Download the text files for these works, or copy the raw text
from your browser into a text file on your computer. You can use the count()
method to find out how many times a word or phrase appears in a string.
Notice that converting the string to lowercase using lower() catches all
appearances of the word you're looking for, regardless of how it's formatted.
Write a program that reads the files you found at Project Gutenberg and
determines how many times the word 'the' appears in each text.
This will be an approximation because it will also count words such as 'then'
and 'there'. Try counting 'the ', with a space in the string, and see how much lower your count is."""

from module_file_reader import FileReader


def count_words(content, word):
    """
    Count the number of occurrences of a word in a given content.

    Args:
        content (str): The text content in which to count the occurrences of the word.
        word (str): The word to count within the content.

    Returns:
        int: The number of times the word appears in the content, case-insensitive.
    """
    return content.lower().count(word.lower())


reader = FileReader()
reader.add_files()
contents = reader.read_files()

text = input("What word do you want to use to count? ")

for file_path, content in contents.items():
    word_count = count_words(content, text)
    print(f"File: {file_path}")
    print(f"Number of times the word '{text}' appeared in the text: {word_count}")
