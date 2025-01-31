"""All versions of foods.py in this section have avoided using for loops when printing, to save space.
Choose a version of foods.py, and write two for loops to print each list of foods."""

my_foods = ["Pizza", "Falafel", "Carrot Cake"]
friend_foods = my_foods[:]

my_foods.append("Cannoli")
friend_foods.append("Ice cream")

print("\nMy favorite foods are:")
for foods in my_foods:
    print(foods)

print("\nMy friend's favorite foods are:")
for foods in friend_foods:
    print(foods)
