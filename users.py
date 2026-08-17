class User: 
    """An attemp to model a simple user."""
    def __init__(self, first_name, last_name, age, country): 
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.login_attempts = 0

    def describe_user(self): 
        """Print a summary about the user."""
        print(f"{self.first_name} {self.last_name} is {self.age} years old and is from {self.country}.")
    
    def greet_user(self): 
        """greets the user"""
        print(f"Welcome {self.first_name}, you are {self.age} years old today.")

    def increment_login_attempts(self): 
        self.login_attempts+=1

    def reset_login_attempts(self): 
        self.login_attempts = 0


