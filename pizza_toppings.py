message = "Please enter a topping for you pizza."
message += "\nType 'quit' to finish your toppings order.\n"

while True: 
    topping = input(message)
    
    if topping == "quit": 
        break
    else: 
        print(f"One {topping} added!")

