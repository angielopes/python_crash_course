"""Write a function called make_shirt() that accepts a size and the text
of a message that should be printed on the shirt.
The function should print a sentence summarizing the size of the shirt and
the message printed on it. Call the function once using positional arguments to make a shirt.
Call the function a second time using keyword arguments."""


def make_shirt(size, message):
    print(f"\nThe shirt's size is {size} and the message that will be print on it is:")
    print(f"{message}")


make_shirt("XL", "This is what ask for\nHeavy is the crow!!!!!!!!")
make_shirt(size="S", message="Is something that you do to me\nI run away like mercury")
