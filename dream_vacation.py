dream_vacations = {}
poll_active = True

while poll_active: 
    name = input("What is your name?\n")
    place = input("Where is your dream vacation?\n")
    dream_vacations[name] = place

    repeat = input("Would you like to let another person respond? (yes/no)\n")
    if repeat == "no": 
        poll_active = False

print("\n--- Poll Results ---")
for name, vacation in dream_vacations.items(): 
    print(f"{name} would like to go to {vacation}.")

