sandwiches = ["turkey bacon", "pastrami", "pastrami", "pastrami", "italian queen", "lean chicken", "Canadian hero"]
finished_sandwiches = []

print("The deli has ran out of pastrami!")
while "pastrami" in sandwiches: 
    sandwiches.remove("pastrami")


while sandwiches: 
    current_sandwich = sandwiches.pop()
    finished_sandwiches.append(current_sandwich)

    print(f"I made your {current_sandwich}!")

print(finished_sandwiches)
