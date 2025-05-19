
#Docstring-Python docstrings are strings used right after the definition of a function, method, class, or module.
def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__)
# The __doc__ attribute is a string that contains the documentation string for the function.
# It is a good practice to include a docstring in your functions to describe what they do.
# The docstring can be accessed using the __doc__ attribute of the function.
def add(a,b):
    sum=a+b
    '''This function takes two numbers and returns their sum'''
    return sum
print(add(2,3))
print(add.__doc__)
import this#the zen of python
# The Zen of Python is a collection of guiding principles for writing computer programs in the Python language.