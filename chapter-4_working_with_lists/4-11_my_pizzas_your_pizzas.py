"""Start with your program from Exercise 4-1 (page 56).
Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message 'My favorite pizzas are:',
and then use a for loop to print the first list.
Print the message 'My friend's favorite pizzas are:', and then use a for loop to print the second list.
Make sure each new pizza is stored in the appropriate list."""

my_pizzas = ["Muzzarela", "Lombo", "Calabresa"]
friend_pizzas = my_pizzas[:]

# Adicionando uma pizza nova à lista original
my_pizzas.append("Pepperoni")

# Adicionando uma pizza diferente à lista do meu amigo
friend_pizzas.append("Primavera")

# Provando que as listas são diferentes
print(f"\nMinhas pizzas favoritas são:")
for pizza in my_pizzas:
    print(pizza)
print(f"\nAs pizzas favoritas do meu amigo são:")
for pizza in friend_pizzas:
    print(pizza)