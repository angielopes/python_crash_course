"""Write a function called favorite_book() that accepts one parameter, title.
The function should print a message, such as One of my favorite books is Alice in Wonderland.
Call the function, making sure to include a book title as an argument in the function call."""


def favorite_book(title):
    print(
        f"I dont know if this is my favorite book (because there are a lot), but one of my favorite books is {title.title()}."
    )


favorite_book("neuromancer")
