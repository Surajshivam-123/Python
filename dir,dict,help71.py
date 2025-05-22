#dir(): The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object. It is a useful tool for discovering what you can do with an object.
x=[1,23,4]
print(dir(x))

#__dict__: The __dict__ attribute is a dictionary that contains the object's writable attributes. It is a useful way to see the internal state of an object and what attributes it has.
class MyClass:
    def __init__(self):
        self.attr1 = 1
        self.attr2 = 2
obj1=MyClass()
print(obj1.__dict__)

#help(): The help() function is used to get help documentation for an object, including a description of its attributes and methods.

print(help(list.append))
# The help() function can also be used to get help on a specific method of an object.