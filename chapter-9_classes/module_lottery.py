"""
This module defines a Lottery class that simulates a lottery system by drawing
random numbers.

Classes:
    Lottery: A class to represent a lottery system that draws random numbers."""

from random import sample


class Lottery:
    """
    A class to represent a lottery system that draws random numbers.

    Attributes
    ----------

    numbers_letters : list
        A list of numbers that can be drawn in the lottery.
    results : list
        A list to store the drawn numbers.

    Methods
    -------

    draw():
        Draws 4 random numbers or letters from the `numbers` list.
    show_results():
        Prints the drawn numbers.
    """

    def __init__(self):
        """
        Initialize the lottery with a list of numbers.

        Attributes:
            numbers_letters (list): A list containing integers representing the lottery elements.
        """
        self.numbers = range(1, 20)

    def draw(self):
        """
        Draws a random sample of 4 elements from the numbers list.

        Returns:
            list: A list containing 4 randomly selected elements from numbers.
        """
        self.results = sorted(sample(self.numbers, 4))
        return self.results

    def show_results(self):
        """
        Display the results of the lottery draw.

        This method prints out the numbers and letters that were drawn in the lottery.
        It iterates through the `results` attribute of the instance and prints each
        result.
        """
        print(f"The numbers and letters drawn were: {self.results}")
