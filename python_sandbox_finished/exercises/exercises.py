# Unit 1 Exercises & Homework Assignment

# Exercise 1: Use the Python Interpreter to create different types of variables.
# I created these variables using the Python Interpreter:

x = 1
y = 1.5
name = 'Carrie'
is_cool = True

# Exercise 2: Use the Python Interpreter to try assigning values to variables and then using the conditionals and comparison operators.
# I tried out these comparisons with my variables:

print (x < y)
print (x > y)
print (x != y)
print (x == y)
print (x >= y)
print (x <= y)

# Exercise 3: Use VS Code to develop a Hello World program in Python.

if name == 'Carrie':
    print ("Hello World!")

def goodnight_moon():
    print ("Goodnight, Moon.")

goodnight_moon()

# Homework: Create a python function that Calculates the area of a circle given its radius.

# For this function, findArea(r) specifies that the function being defined takes one variable.
def findArea(r):
    PI = 3.142
    return PI * (r*r);

# The radius we're working with here is 5.
print(findArea(5))

# This is more complicated
# %.6f is a format specifier that tells Python to format the answer as a float with 6 decimal places.
# % is the modulo operator to combine the format specifier with the result of the function.

print ("Area is %.6f" % findArea(5))

# This one uses an imported module (math).

import math
def FINDarea(r):
  area = math.pi* pow(r,2)
  return print('Area of circle is:' ,area)
FINDarea(4)

'''
When the Python interpreter encounters a `return` statement, it immediately stops executing the rest of the code in the function, regardless of whether there are more 
lines of code after it.

The `return` statement can optionally be followed by an expression. The value of this expression is then sent back to the part of the code that called the function. If no 
expression is provided, the function returns `None`.

The `return` statement can only be used inside a function. It is not valid in other parts of the Python code.
'''