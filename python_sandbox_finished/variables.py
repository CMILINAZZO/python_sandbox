# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a function's purpose).
These can use either single or double quotes.
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive. (name and NAME are different variables.)
  - They must start with a letter or an underscore.
  - They can have numbers but cannot start with one.
"""

# x = 1           # int (integer)
# y = 2.5         # float
# name = 'John'   # str (string)
# is_cool = True  # bool (Boolean)

# Is it just me or do integers seem a bit useless?

# Multiple assignment - This is more compact than listing them separately.
x, y, name, is_cool = (1, 2.5, 'John', True)

# Basic math
a = x + y

# Casting
x = str(x)
y = int(y) 
z = float(y)

print(type(z), z)