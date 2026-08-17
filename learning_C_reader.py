from pathlib import Path

path = Path('files/learning_python.txt')
contents = path.read_text()

contents = contents.replace('Python', 'C')
print(contents)
