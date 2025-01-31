"""Make a list or tuple containing a series of 10 numbers and 5 letters.
Randomly select 4 numbers or letters from the list and print a message
saying that any ticket matching these 4 numbers or letters wins a prize."""

from random import sample


class Lottery:
    """
    A class to represent a lottery system that draws random numbers and letters.

    Attributes
    ----------

    numbers_letters : list
        A list of numbers and letters that can be drawn in the lottery.
    results : list
        A list to store the drawn numbers and letters.

    Methods
    -------

    draw():
        Draws 4 random numbers or letters from the numbers_letters list.
    show_results():
        Prints the drawn numbers and letters.
    """

    def __init__(self):
        """
        Initialize the lottery with a list of numbers and letters.

        Attributes:
            numbers_letters (list): A list containing integers and strings
                                    representing the lottery elements.
        """
        """"""
        self.numbers_letters = [
            67,
            45,
            23,
            34,
            12,
            9,
            97,
            32,
            54,
            76,
            "S",
            "F",
            "B",
            "Ç",
            "V",
        ]

    def draw(self):
        """
        Draws a random sample of 4 elements from the numbers_letters list.

        Returns:
            list: A list containing 4 randomly selected elements from numbers_letters.
        """
        self.results = sample(self.numbers_letters, 4)
        return self.results

    def show_results(self):
        """
        Display the results of the lottery draw.

        This method prints out the numbers and letters that were drawn in the lottery.
        It iterates through the `results` attribute of the instance and prints each
        result. Finally, it prints a message indicating that if the user's ticket
        contains these values, they will win a prize.
        """
        print("The numbers and letters drawn were:")
        for result in self.results:
            print(f"- {result}")
        print("If your ticket has these values, you will win a prize.")


my_ticket = Lottery()
my_ticket.draw()
my_ticket.show_results()
