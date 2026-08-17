sandwiches = ["turkey bacon", "italian queen", "lean chicken", "Canadian hero"]
finished_sandwiches = []

while sandwiches: 
    current_sandwich = sandwiches.pop()
    finished_sandwiches.append(current_sandwich)

    print(f"I made your {current_sandwich}!")

print(finished_sandwiches)
