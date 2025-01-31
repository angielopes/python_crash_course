"""Using your latest Restaurant class, store it in a module.
Make a separate file that imports Restaurant.
Make a Restaurant instance, and call one of Restaurant's methods
to show that the import statement is working properly."""

from module_restaurant import Restaurant

my_restaurant = Restaurant("Rosie's Diner", "Classic American Diner")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
