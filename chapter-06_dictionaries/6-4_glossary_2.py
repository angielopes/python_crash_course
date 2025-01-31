"""Now that you know how to loop through a dictionary, clean up the code
from Exercise 6-3 (page 99) by replacing your series of print() calls with
a loop that runs through the dictionary's keys and values.
When you're sure that your loop works, add five more Python terms to your glossary.
When you run your program again, these new words and meanings should automatically be included in the output."""

list_glossary = {
    "list": "collection of items",
    "append": "add new item to the end of the list",
    "insert": "add new item to specific position on the list",
    "pop": "remove last item of the list",
    "sort": "permanently organize the list",
}

for key, values in list_glossary.items():
    print(f"{key.title()}\n{values.capitalize()}\n")
