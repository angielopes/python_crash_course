"""Modify the make_shirt() function so that shirts are large by default
with a message that reads I love Python. Make a large shirt and a medium
shirt with the default message, and a shirt of any size with a different message."""


def make_shirt(message, size="L"):
    print(f"\nThe shirt's size is {size} and the message that will be print on it is:")
    print(f"{message}")


make_shirt("I love Python!")


def make_shirt(size, message="I love Python!"):
    print(f"\nThe shirt's size is {size} and the message that will be print on it is:")
    print(f"{message}")


make_shirt("M")
