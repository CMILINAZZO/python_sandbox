# A function is a block of code which only runs when it is called. In Python, we do not use curly brackets, we use indentation with tabs or spaces


# Create function
# This would be a really unlikely function, is only here for the sake of example.
def sayHello(name='Sam'):
    print(f'Hello {name}')


# Return values
# This sort of function is much more common.
def getSum(num1, num2):
    total = num1 + num2
    return total


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2: num1 + num2

print(getSum(10, 3))

# So the difference here is that you don't need to define the 'total' variable?
# Settings > format on save > false
# If the settings aren't right, it will change the function.