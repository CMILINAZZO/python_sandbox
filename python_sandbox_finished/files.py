# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile = open('myfile.txt', 'w')

# Get some info
print('Name: ', myFile.name)
print('Is Closed : ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.write('I love Python')
myFile.write(' and JavaScript')
myFile.close()

# Append to file
myFile = open('myfile.txt', 'a')
myFile.write(' I also like PHP')
myFile.close()

# Read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)

'''
You don't want to use open, write and close in real development, it is prone to vulnerabilities.
Use 'with' instead. It ensures that the file is automatically closed even if an exception occurs.

Play around with this.

Converting CSV to JSON is a common program. Tom shared some resources to try this out.

w mode is write mode, r mode is read mode
'''

