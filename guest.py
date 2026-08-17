from pathlib import Path
path = Path('files/guest.txt')

name = input("Enter your name: ")

path.write_text(name)
