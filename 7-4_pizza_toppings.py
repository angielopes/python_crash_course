"""Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.
As they enter each topping, print a message saying you'll add that topping to their pizza."""

prompt = "\nPlease, enter a pizza topping."
prompt += "\nOr type 'quit' to exit: "

while True:
    topping = input(prompt)

    if topping == "quit":
        break
    else:
        print(f"We are gonna add {topping.title()} to your pizza.")
