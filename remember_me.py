from pathlib import Path
import json

def get_stored_information(path): 
    """Get stored username if available."""
    if path.exists(): 
        contents = path.read_text()
        information = json.loads(contents)
        return information
    else: 
        return None

def get_username(): 
    """Prompt for a new username."""
    username = input("What is your name? ")
    return username

def get_new_age(): 
    """Prompt for a new age."""
    age = input("How old are you? ")
    return age

def get_new_country(): 
    """Promp for their country of residence."""
    country = input("Which country do you live in? ")
    return country
    
def greet_user(): 
    """Greet the user by name."""
    username = get_username()
    
    path = Path(f'files/{username}.json')
    information = get_stored_information(path)

    if information: 
        print(f'Welcome back, {information["username"]}!')
       
        print(f'We have your information! You are {information["age"]} years old and live in {information["country"]}!')
        
    else:
        print(f"It looks like we don't have your information {username}.")
        age = get_new_age()
        country = get_new_country()

        information = {
            "username": username, 
            "age" : age, 
            "country" : country
        }
        contents = json.dumps(information)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}!")

greet_user()
