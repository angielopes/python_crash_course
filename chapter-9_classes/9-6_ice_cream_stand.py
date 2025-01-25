"""An ice cream stand is a specific kind of restaurant.
Write a class called IceCreamStand that inherits from the Restaurant class you
wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 166).
Add an attribute called flavors that stores a list of ice cream flavors.
Write a method that displays these flavors. Create an instance of IceCreamStand,
and call this method."""


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


class IceCreamStand(Restaurant):
    """A class to represent an ice cream stand, which is a specific type of restaurant.

    Attributes:
    ----------
        flavors : list
            A list of ice cream flavors available at the stand.

    Methods:
    ----------
    get_flavors():
        Prints the ice cream's flavors."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the IceCreamStand with a restaurant name, cuisine type, and a list of flavors.

        Args:
            restaurant_name (str): The name of the restaurant.
            cuisine_type (str): The type of cuisine the restaurant offers.
        """
        """"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["chocolate", "vanilla", "mango"]

    def get_flavors(self):

        print(f"{self.restaurant_name}'s flavors:")
        # for flavor in self.flavors.items():
        print(f"{self.flavors}")


ice_cream_restaurant = IceCreamStand("Gelato", "Ice Cream")
ice_cream_restaurant.describe_restaurant()
ice_cream_restaurant.get_flavors()
