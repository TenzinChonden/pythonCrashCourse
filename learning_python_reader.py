from pathlib import Path

path = Path('files/learning_python.txt')
content = path.read_text()

print(content)

lines = content.splitlines()
for line in lines: 
    print(line)
