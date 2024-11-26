from pathlib import Path

# P is capital meaning it is a class

# Absolute Path: F:/codes/Python
# Relative Path


path = Path('F:/codes')

print(path.exists())

for file in path.glob('**/*.py'):
 print(file)




