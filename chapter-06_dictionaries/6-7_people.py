"""Start with the program you wrote for Exercise 6-1 (page 98).
Make two new dictionaries representing different people, and store all
three dictionaries in a list called people.
Loop through your list of people.
As you loop through the list, print everything you know about each person."""

jacira = {"first_name": "jacira", "last_name": "lopes", "age": 58, "city": "marília"}
pedro = {"first_name": "pedro", "last_name": "lopes", "age": 63, "city": "marília"}
amanda = {"first_name": "amanda", "last_name": "lopes", "age": 35, "city": "marília"}
people = [jacira, pedro, amanda]

for person in people:
    print(f"\n{person['first_name'].capitalize()} {person['last_name'].capitalize()}")
    print(f"First name: {person['first_name'].capitalize()}")
    print(f"Last name: {person['last_name'].capitalize()}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city'].capitalize()}")
