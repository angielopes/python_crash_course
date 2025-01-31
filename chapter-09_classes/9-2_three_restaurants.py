"""Start with your class from Exercise 9-1.
Create three different instances from the class, 
and call describe_restaurant() for each instance."""


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


restaurant_info = {
    "Ichiraku Ramen": "Japanese Ramen",
    "Pizza Planet": "Italian Pizza",
    "Kame House Café": "Tropical Smoothies",
    "Central Perk": "Coffee and Pastries",
    "Gusteau's": "French Cuisine",
    "The Prancing Pony": "Medieval Pub Food",
    "Good Burger": "American Burgers",
    "Baratie": "Seafood",
    "Rosie's Diner": "Classic American Diner",
    "The Three Broomsticks": "British Pub Food and Butterbeer",
}

for name, cuisine in restaurant_info.items():
    restaurant = Restaurant(name, cuisine)
    restaurant.describe_restaurant()
    restaurant.open_restaurant()
