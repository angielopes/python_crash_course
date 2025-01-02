"""You just found out that your new dinner table won't arrive in time for the dinner,
and now you have space for only two guests.
• Start with your program from Exercise 3-6.
Add a new line that prints a message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list.
Each time you pop a name from your list, print a message to that person letting them know you're sorry
you can't invite them to dinner.
• Print a message to each of the two people still on your list, letting them know they're still invited.
• Use del to remove the last two names from your list, so you have an empty list.
Print your list to make sure you actually have an empty list at the end of your program."""

guests = [
    "Felipe",
    "Jacira",
    "Pedro",
    "Amanda",
    "Adriana",
    "André",
    "Raissa",
    "Henrique",
    "Cinthia",
    "Eduardo",
]

print("Quantidade de convidados:")
print(len(guests))

print(
    "Infelizmente a minha grande mesa não chegará a tempo, então só poderei convidar duas pessoas para a minha festa não mais arrasadora."
)

remove_felipe = guests.pop(0)
print(f"Desculpe {remove_felipe} mas você foi desconvidado da minha festa!")

remove_amanda = guests.pop(2)
print(f"Desculpe {remove_amanda} mas você foi desconvidado da minha festa!")

remove_adriana = guests.pop(2)
print(f"Desculpe {remove_adriana} mas você foi desconvidado da minha festa!")

remove_andre = guests.pop(2)
print(f"Desculpe {remove_andre} mas você foi desconvidado da minha festa!")

remove_raissa = guests.pop(2)
print(f"Desculpe {remove_raissa} mas você foi desconvidado da minha festa!")

remove_henrique = guests.pop(2)
print(f"Desculpe {remove_henrique} mas você foi desconvidado da minha festa!")

remove_cinthia = guests.pop(2)
print(f"Desculpe {remove_cinthia} mas você foi desconvidado da minha festa!")

remove_eduardo = guests.pop(2)
print(f"Desculpe {remove_eduardo} mas você foi desconvidado da minha festa!")


for guest in guests:
    print(
        f"Parabéns, {[guest]} você teve sorte e continua convidado para a minha festa!"
    )

print("Quantidade de convidados depois de quase todos serem descondiados:")
print(len(guests))

del guests[:]

print(guests)
print("Quantidade de convidados final:")
print(len(guests))
