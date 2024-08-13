# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Carrie'
age = 26


# Concatenate
print('Hello, my name is ' + name + ' and I am ' + str(age))

'''
print('Hello, my name is ' + name + ' and I am ' + age)
^ This won't work because you can't insert an integer into a string
'''

# String Formatting

# Arguments by position
print('Hello, my name is {name} and I am {age}'.format(name=name, age=age))
# Age stays an int, so you can do math with it:
print('Hello, my name is {name} and I am {age}'.format(name=name, age=(age+100)))


# F-Strings (3.6+)
print(f'Hello, my name is {name} and I am {age}')
# This seems a lot more straightforward if you want to do math with the int:
print(f'Hello, my name is {name} and I am {age+100}')

# String Methods

s = 'hello world'

# Capitalize string
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())

'''
test = 'string'
print(len(test))
print(test.find('s'))
'''
