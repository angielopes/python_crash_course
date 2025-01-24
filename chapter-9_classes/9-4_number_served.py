"""Start with your program from Exercise 9-1 (page 162).
- Add an attribute called number_served with a default value of 0.
- Create an instance called restaurant from this class.
- Print the number of customers the restaurant has served,
and then change this value and print it again.
- Add a method called set_number_served() that lets you set the
number of customers that have been served.
- Call this method with a new number and print the value again.
- Add a method called increment_number_served() that lets you increment
the number of customers who've been served.
- Call this method with any number you like that could represent how
many customers were served in, say, a day of business."""


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
        self.number_served = 0

    def describe_restaurant(self):
        """Prints the restaurant's name and the type of cuisine it serves.

        This method uses the attributes `restaurant_name` and `cousine_type`
        of the instance to display a descriptive message about the restaurant.

        """
        print(
            f"\nThe {self.restaurant_name} restaurant specializes in {self.cuisine_type}",
            end=" ",
        )

    def open_restaurant(self):
        """Informs if the restaurant is open or not."""
        print(f"is now open!")

    def set_number_served(self):
        """Shows how many costumers were served in the restaurant."""
        print(f"And has already served {self.number_served} customers :)")

    def increment_number_served(self, customers):
        """Add the given amount to the number of customers served."""
        self.number_served += customers


my_restaurant = Restaurant("Ichiraku Ramen", "Japanese Ramen")
my_restaurant.number_served = 6
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.increment_number_served(4)
my_restaurant.set_number_served()
