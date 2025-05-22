#Access specifiers or access modifiers in python programming are used to limit the access of class variables and class methods outside of class while implementing the concepts of inheritance.
'''Types of access specifiers
Public access modifier
Private access modifier
Protected access modifier'''

#Public access modifier-all the variables and methods (member functions) in python are by default public.
class PublicAccess:
    def __init__(self):
        self.public_variable = "I am a public variable"
    def public_method(self):
        return self.public_variable
#Creating an object of the class
obj = PublicAccess()
print(obj.public_variable)

#Private access modifier-Private members are not accessible from outside the class. They are only accessible within the class in which they are declared. Private members are declared by adding double underscore (__) before the member name.
class PrivateAccess:
    def __init__(self):
        self.__private_variable ="I am a private variable"
    def __private_fun(self):
        print("I am a private function")
    def private_method(self):
        return self.__private_variable
#Creating an object of the class
obj = PrivateAccess()
# print(obj.__private_variable) # This will raise an AttributeError
# print(obj.__private_fun()) # This will also raise an AttributeError
print(obj.private_method()) # This will not raise an AttributeError
#To access private members from outside the class, we can use name mangling. Name mangling is a technique used to change the name of a variable in a way that makes it harder to create subclasses that accidentally override the private attributes and methods.   
print(obj._PrivateAccess__private_variable) # This will work

#Protected access modifier- Protected members are not accessible from outside the class but they are accessible in the derived class. Protected members are declared by adding a single underscore (_) before the member name.
class ProtectedAccess:
    def __init__(self):
        self._protected_variable="I am a protected variable"
    def _protected_fun(self):
        print("I am a protected function")
    def protected_method(self):
        return self._protected_variable
class Derived(ProtectedAccess):
    def __init__(self):
        super().__init__()
        print(self._protected_variable) # This will work
        self._protected_fun() # This will also work
#Creating an object of the class
obj = Derived()
obj2= ProtectedAccess()
#single underscore is just a naming convention, and does not actually provide any protection or restrict access to the member
print(obj2._protected_variable) # This will  not raise an AttributeError
print(obj._protected_variable) # This will work

