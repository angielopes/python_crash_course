"""Write a program that asks the user how many people are in their dinner group.
If the answer is more than eight, print a message saying they'll have to wait for a table.
Otherwise, report that their table is ready."""

amount_people = input("How many people will have dinner with us? ")
amount_people = int(amount_people)

if amount_people <= 8:
    print("The table awaits you!")
else:
    print("You will have to wait a moment to get a table.")
