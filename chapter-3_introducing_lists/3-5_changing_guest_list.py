"""You just heard that one of your guests can't make the dinner, so you need to send out a new set of invitations.
You'll have to think of someone else to invite.
• Start with your program from Exercise 3-4.
Add a print() call at the end of your program, stating the name of the guest who can't make it.
• Modify your list, replacing the name of the guest who can't make it with the name of
the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in your list."""

guests = ["Jacira", "Pedro", "Amanda", "André", "Raissa", "Henrique", "Anézia"]

for guest in guests:
    print(
        f"Olá, {[guest]}! Convido você para a minha festa super arrasadora. Não perca :)"
    )

print(f"A {guests[-1]} infelizmente não conseguirá ir à festa :(")

guests[-1] = "Cinthia"

for guest in guests:
    print(
        f"Olá, {[guest]}! Convido você para a minha festa super arrasadora. Não perca :)"
    )

print("Quantidade de convidados atualizada:")
print(len(guests))
