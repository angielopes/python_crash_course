"""Make a list called sandwich_orders and fill it with the names of various sandwiches.
Then make an empty list called finished_sandwiches.
Loop through the list of sandwich orders and print a message for each order,
such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches.
After all the sandwiches have been made, print a message listing each sandwich that was made."""

sandwish_orders = [
    "Turkey and Cheese Sandwich",
    "Ham and Swiss Sandwich",
    "Chicken Salad Sandwich",
    "BLT Sandwich",
    "Egg Salad Sandwich",
    "Tuna Melt Sandwich",
    "Grilled Cheese Sandwich",
    "Club Sandwich",
    "Veggie Sandwich",
    "Roast Beef Sandwich",
]

finished_sandwishes = []

while sandwish_orders:
    current_order = sandwish_orders.pop()

    print(f"I've made your {current_order}!")
    finished_sandwishes.append(current_order)

print("\nReady-made sandwiches:")
for sandwish in finished_sandwishes:
    print(sandwish)
