"""Modify your program from Exercise 6-2 (page 98) so each person can have more than one favorite number.
Then print each person's name along with their favorite numbers."""

favorite_numbers = {
    "angela": [13, 67, 89],
    "totoro": [25, 12, 34],
    "kiki": [4, 6, 8],
    "chiriro": [63, 45, 50],
    "nemo": [8, 1, 0],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(number, end=" ")
