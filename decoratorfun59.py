#decorator function
def greet(fx):
    def inner(*args,**kwargs):
        print("Hello, welcome!")
        fx(*args,**kwargs)
    return inner

@greet
def display(name):
    print("Name is",name)

def add(x,y,z):
    print("Sum is",x+y+z)

@greet
def welcome():
    print("Welcome to the world of decorators")
welcome()
greet(add)(5,10,1)
display("Suraj")

#practical use
import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b
print(my_function(3, 4))