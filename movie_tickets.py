message = "What is your age?\n"

while True: 
    age = input(message)
    age = int(age)

    if age < 3: 
        print("Your ticket is free!")
    elif age >= 3 and age <= 12: 
        print("Your ticket is $10.")
    else: 
        print("Your ticket is $15.")
    
    is_next = input("continue to next user?\ny/n\n")

    if is_next == "y": 
        continue
    else: 
        break
