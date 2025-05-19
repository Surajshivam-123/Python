def greet(name):
    print("Hello, ",name)
greet("Donald Trump")
#four types of arguments
''' Default Arguments
    Keyword Arguments
    Variable length Arguments
    Required Arguments
'''
# Default Arguments
def greet(name, msg="Good morning!"):
    print("Hello", name + ', ' + msg)
greet("Donald Trump")
greet("Donald Trump", "Good evening!")
# Keyword Arguments
def greet(name, msg):
    print("Hello", name + ', ' + msg)
greet(msg="Good morning!", name="Donald Trump")
greet(name="Donald Trump", msg="Good evening!")
# Variable length Arguments
def greet(*names):
    for name in names:
        print("Hello", name)
greet("Donald Trump", "Barack Obama", "George Bush")#function accesses the arguments by processing them in the form of tuple.
# Required Arguments
def greet(name, msg):
    print("Hello", name + ', ' + msg)
greet("Donald Trump", "Good morning!")
greet("Donald Trump", "Good evening!")
#Keyword Arbitrary Arguments:
def wel(**name):#function accesses the arguments by processing them in the form of dictionary.
    print("Hello",name["fname"],name["mname"],name["lname"])
wel(fname="Donald", mname="John", lname="Trump")
def add(a,b):
    return a+b
print(add(2,3))

