class Restaurant: 
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant_name and cuisine_type attributes."""
 
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self): 
        """Prints two pieces of information about the restaurant."""
        print(f"{self.restaurant_name} is a fantastic {self.cuisine_type} restaurant!")

    def open_restaurant(self): 
        """Indicates that the restaurant is open."""
        print(f"{self.restaurant_name} is open!")

restaurant = Restaurant("Momo Ghar", "Himalayan")
pizza_pizza = Restaurant("Pizza Pizza", "Italian")
mcDonalds = Restaurant("McDonalds", "American")

restaurant.describe_restaurant()
pizza_pizza.describe_restaurant()
mcDonalds.describe_restaurant()
