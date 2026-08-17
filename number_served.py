class Restaurant: 
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant_name and cuisine_type attributes."""
 
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self): 
        """Prints two pieces of information about the restaurant."""
        print(f"{self.restaurant_name} is a fantastic {self.cuisine_type} restaurant!")

    def open_restaurant(self): 
        """Indicates that the restaurant is open."""
        print(f"{self.restaurant_name} is open!")

    def set_number_served(self, number): 
        self.number_served = int(number)

    def increment_number_served(self): 
        self.number_served+=1


restaurant = Restaurant("Momo Ghar", "Himalayan")
print(restaurant.number_served)

restaurant.number_served  = 10
print(restaurant.number_served)

restaurant.set_number_served(12)
print(restaurant.number_served)

restaurant.increment_number_served()
print(restaurant.number_served)


