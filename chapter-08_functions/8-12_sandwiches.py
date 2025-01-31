"""Write a function that accepts a list of items a person wants on a sandwich.
The function should have one parameter that collects as many items as the
function call provides, and it should print a summary of the sandwich that's being ordered.
Call the function three times, using a different number of arguments each time."""


def sandwiches_orders(*fillings):
    """Print the list of fillings that have been requested."""
    print("Adding the following fillings to your sandwich:")
    for filling in fillings:
        print(f"- {filling.title()}")


sandwiches_orders("tomato", "hamburger")
sandwiches_orders("lettuce", "tomato", "cheese")
sandwiches_orders("picles", "chicken breast")
