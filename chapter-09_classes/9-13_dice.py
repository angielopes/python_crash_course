"""Make a class Die with one attribute called sides, which has a default
value of 6. Write a method called roll_die() that prints a random number
between 1 and the number of sides the die has. Make a 6-sided die and roll
it 10 times. Make a 10-sided die and a 20-sided die. Roll each die 10 times."""

from random import randint


class Die:
    """
    A class to represent a die.

    ...

    Attributes
    ----------
    sides : int
        number of sides on the die (default is 6)

    Methods
    -------

    roll_dice(roll_times):
        Rolls the die a specified number of times and prints the result.
    """

    def __init__(self, sides=6):
        """
        Initialize a new instance of the class.

        Args:
            sides (int, optional): The number of sides on the dice. Defaults to 6.
        """
        self.sides = sides

    def roll_dice(self, roll_times):
        """
        Simulate rolling the dice a specified number of times and print the results.

        Args:
            roll_times (int): The number of times to roll the dice.

        Returns:
            None
        """
        for roll in range(roll_times):
            print(f"{randint(1, self.sides)}", end=" | ")


print("Roll the 6-sided die 10 times:")
my_roll = Die(6)
my_roll.roll_dice(10)

print("\n")
print("Roll the 10-sided die 20 times:")
my_roll = Die(10)
my_roll.roll_dice(20)
