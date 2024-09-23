# Read Lines
with open('example_text.txt', 'r') as f:
    text = f.readlines()
    print(text) # returns a list
    print(f.name)
    print(f.mode)
    print(f.closed)
