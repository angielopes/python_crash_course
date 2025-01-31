"""A buffet-style restaurant offers only five basic foods.
Think of five simple foods, and store them in a tuple.
• Use a for loop to print each food the restaurant offers. OK
• Try to modify one of the items, and make sure that Python rejects the change. OK
• The restaurant changes its menu, replacing two of the items with different foods.
Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu."""

simple_foods = ("Pizza", "Pasta", "Salad", "Cake", "Ice Cream")

print("All of our simple foods:")
for food in simple_foods:
    print(food)

# Modifying one of the itens
# simple_foods[2] = "Buger"

# New menu replacing two itens
simple_foods = ("Pizza", "Pasta", "Burger", "Cake", "Brigadeiro")
print("\nOur new menu of simple foods:")
for food in simple_foods:
    print(food)
