"""Write different versions of either Exercise 7-4 or 7-5 that do each of the following at least once:
• Use a conditional test in the while statement to stop the loop.
• Use an active variable to control how long the loop runs.
• Use a break statement to exit the loop when the user enters a 'quit' value."""

prompt = "Please, enter a pizza topping."
prompt += "\nOr type 'quit' to exit: "


print("CONDICIONAL TEST")
topping = ""
while topping != "quit":
    topping = input(prompt).strip()

    if topping.lower() != "quit":
        print(f"We are gonna add {topping.title()} to your pizza.")


print("\nACTIVE VARIABLE")
active = True
while active:
    topping = input(prompt).strip()

    if topping.lower() == "quit":
        active = False
    else:
        print(f"We are gonna add {topping.title()} to your pizza.")


print("\nBREAK STATEMENT")
while True:
    topping = input(prompt).strip()

    if topping.lower() == "quit":
        break
    else:
        print(f"We are gonna add {topping.title()} to your pizza.")
