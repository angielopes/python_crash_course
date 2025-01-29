"""Make a list or tuple containing a series of 10 numbers and 5 letters.
Randomly select 4 numbers or letters from the list and print a message
saying that any ticket matching these 4 numbers or letters wins a prize."""

from random import sample

numbers_letters = [67, 45, 23, 34, 12, 9, 97, 32, 54, 76, "S", "F", "B", "Ç", "V"]

results = sample(numbers_letters, 4)

print("The numbers and letters drawn were:")
for result in results:
    print(f"- {result}")
print("If your ticket has these values, you will win a prize.")
