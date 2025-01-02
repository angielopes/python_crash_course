"""If you could invite anyone, living or deceased, to dinner, who would you invite?
Make a list that includes at least three people you'd like to invite to dinner.
Then use your list to print a message to each person, inviting them to dinner."""

guests = ["Jacira", "Pedro", "Amanda", "André", "Raissa", "Henrique", "Anézia"]

for guest in guests:
    print(
        f"Olá, {[guest]}! Convido você para a minha festa super arrasadora. Não perca :)"
    )

print(guests)

print("Quantidade de convidados:")
print(len(guests))
