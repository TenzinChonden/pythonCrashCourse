
print("This is a addition loop. Type 'done' to get your total.")
total = 0

while True: 
    num = input("Enter a number: ")
    if num == "done": 
        break

    try: 
        total += int(num)
    except ValueError: 
        pass

print(f"Your total is: {total}")
