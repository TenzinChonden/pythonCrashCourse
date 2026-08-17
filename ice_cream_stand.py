from restaurant import Restaurant 

class IceCreamStand(Restaurant): 

    """Modeling a simple ice cream stand."""
    def __init__(self, restaurant_name, *flavors):
        """Initialize attributes of the parent class."""
        super().__init__(restaurant_name, cuisine_type="Ice Cream") 
        self.flavors = flavors
 
    def display_flavors(self): 
        print(self.flavors)

my_stand = IceCreamStand("Tenzin's Ice Cream", "Chocolate", "Vanilla", "Pistaccio")

my_stand.display_flavors()  
