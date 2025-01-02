"""Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the
following:
• Print the message 'The first three items in the list are:'.
Then use a slice to print he first three items from that program's list. OK
• Print the message 'Three items from the middle of the list are:'.
Then use a slice to print three items from the middle of the list. OK
• Print the message 'The last three items in the list are:'.
Then use a slice to print the last three items in the list. OK"""

drinks = [
    "Café",
    "Pinga",
    "Caipirinha",
    "Suco de maracujá",
    "Pingado",
    "Cerveja",
    "Vinho",
]

# Primeiros três itens
print("\nPrimeiras três bebidas:")
for drink in drinks[:3]:
    print(drink)

# Três itens do meio
print("\nAs três bebidas do meio:")
for drink in drinks[2:5]:
    print(drink)

# Três últimos itens
print("\nTrês últimas bebidas:")
for drink in drinks[-3:]:
    print(drink)
