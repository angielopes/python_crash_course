"""Write a program that polls users about their dream vacation.
Write a prompt similar to If you could visit one place in the world, where would you go?
Include a block of code that prints the results of the poll."""

dream_vacation = {}

polling_active = True
while polling_active:
    name = input("\nWhat's your name? ").strip()
    place = input(
        "If you could visit one place in the world, where would you go? "
    ).strip()

    dream_vacation[name] = place

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == "no":
        polling_active = False

print("\nDream Vacation Result (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")
for name, place in dream_vacation.items():
    print(f"{name} would love to have a vacation in {place}")
