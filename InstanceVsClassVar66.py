#Class Variables
'''Class variables are defined at the class level and are shared among all instances of the class.
 They are defined outside of any method and are usually used to store information that is common to all instances of the class.'''

#Instance Variables
'''Instance variables are defined at the instance level and are unique to each instance of the class.
 They are defined inside the init method and are usually used to store information that is specific to each instance of the class'''
class Dog:
    # Class variable
    species = "Canis familiaris"
    count = 0  # Class variable to keep track of the number of Dog instances
    def __init__(self, name, age):
        Dog.count+=1  # Increment the count when a new instance is created
        self.name = name  # Instance variable
        self.age = age    # Instance variable
d1= Dog("Buddy", 3)
d2= Dog("Max", 5)
d3= Dog("Bella", 2)
print(f"Dog 1: {d1.name}, Age: {d1.age}, Species: {d1.species}, Count: {d1.count}")
print(f"Dog 2: {d2.name}, Age: {d2.age}, Species: {Dog.species}, Count: {Dog.count}")