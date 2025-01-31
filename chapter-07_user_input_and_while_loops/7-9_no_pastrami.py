"""Using the list sandwich_orders from Exercise 7-8,
make sure the sandwich 'pastrami' appears in the list at least three times.
Add code near the beginning of your program to print a message saying the deli
has run out of pastrami, and then use a while loop to remove all occurrences
of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches."""

sandwish_orders = [
    "Turkey and Cheese Sandwich",
    "Ham and Swiss Sandwich",
    "Pastrami Sandwish",
    "Chicken Salad Sandwich",
    "BLT Sandwich",
    "Egg Salad Sandwich",
    "Pastrami Sandwish",
    "Tuna Melt Sandwich",
    "Grilled Cheese Sandwich",
    "Club Sandwich",
    "Veggie Sandwich",
    "Roast Beef Sandwich",
    "Pastrami Sandwish",
]

print("We are out of Pastrami Sandwish!")

finished_sandwishes = []

while "Pastrami Sandwish" in sandwish_orders:
    sandwish_orders.remove("Pastrami Sandwish")

while sandwish_orders:
    current_order = sandwish_orders.pop()

    print(f"I've made your {current_order}!")
    finished_sandwishes.append(current_order)

print("\nReady-made sandwiches:")
for sandwish in finished_sandwishes:
    print(sandwish)
