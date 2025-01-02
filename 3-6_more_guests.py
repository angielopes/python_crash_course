"""You just found a bigger dinner table, so now more space is available.
Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5.
Add a print() call to the end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list."""

guests = ["Jacira", "Pedro", "Amanda", "André", "Raissa", "Henrique", "Cinthia"]

guests.insert(0, "Felipe")
guests.insert(4, "Adriana")
guests.append("Eduardo")

for guest in guests:
    print(f"A festa ficou maior ainda! Não perca, {[guest]} :)))")

print(guests)
print("Quantidade de convidados atualizada:")
print(len(guests))
