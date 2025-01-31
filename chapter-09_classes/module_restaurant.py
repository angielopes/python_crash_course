"""This module defines the Restaurant class, which represents a restaurant with a name and cuisine type.
Classes:
    Restaurant: A class to represent a restaurant with methods to describe and open the restaurant."""


class Restaurant:
    """A class to represent a restaurant.

    Attributes
    ----------
    restaurant_name : str
        The name of the restaurant
    cuisine_type : str
        The type of cuisine the restaurant serves


    Methods
    -------
    describe_restaurant():
        Prints the restaurant's name and the type of cuisine it serves.
    open_restaurant():
        Prints a message indicating that the restaurant is open.
    """

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant with a name and cuisine type.

        Parameters
        ----------
        restaurant_name : str
            The name of the restaurant.
        cuisine_type : str
            The type of cuisine the restaurant serves.
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints the restaurant's name and the type of cuisine it serves.

        This method uses the attributes `restaurant_name` and `cousine_type`
        of the instance to display a descriptive message about the restaurant.

        """
        print(
            f"\nThe {self.restaurant_name} restaurant specializes in {self.cuisine_type}"
        )

    def open_restaurant(self):
        """Informs if the restaurant is open or not."""
        print(f"And the {self.restaurant_name} is now open!")
