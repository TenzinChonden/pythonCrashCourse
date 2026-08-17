from pathlib import Path

path = Path('files/guest_book.txt')

guest_list = ""

print("Type 'done' to stop entering guests")

while True: 
    name = input("Enter guest name: ")
    
    if name == "done": 
        break
    else: 
        guest_list += name + "\n"

path.write_text(guest_list)
print("Guest book closed.")
