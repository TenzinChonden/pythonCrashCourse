from users import User

class Privileges: 
    """A simple model for a list of privileges."""

    def __init__(self, privileges=()): 
        """Initiating the privilege argument to the instance."""
        self.privileges = privileges

    def show_privileges(self): 
        """Printing each privilege for the admin instance."""
        print("Admin privileges:\n")
        for privilege in self.privileges: 
            print(f"- {privilege}")

class Admin(User): 

   def __init__(self, first_name, last_name, age, country, *privileges): 
        super().__init__(first_name, last_name, age, country)
        self.privileges = Privileges(privileges)


Kelly = Admin("Kelly", "Lee", "23", "Canada", "can edit", "can post")
Kelly.privileges.show_privileges()
