#Static methods in Python are methods that belong to a class rather than an instance of the class.
#defined using the @staticmethod decorator and do not have access to the instance of the class (i.e. self)
class Car:
   @staticmethod
   def start_engine():
      print("Engine started")
Car.start_engine() # Output: Engine started
#Static methods can be called on the class itself, without creating an instance of the class.
#This is useful for utility functions that are related to the class but do not require access to instance-specific data.
#Static methods can also be used to create factory methods that return instances of the class.
class Car:
   @staticmethod
   def create_car(make, model):
      return Car(make, model)
   
   def __init__(self, make, model):
      self.make = make
      self.model = model
   def info(self):
      return f"Car make: {self.make}, model: {self.model}"
object1 = Car.create_car("Toyota", "Camry")
print(object1.info())

#Static methods can also be used to create utility functions that are related to the class but do not require access to instance-specific data.
class MathUtils:
   @staticmethod
   def add(a, b):
      return a + b
   @staticmethod
   def subtract(a, b):
      return a - b
print(MathUtils.add(5, 3)) # Output: 8
print(MathUtils.subtract(5, 3)) # Output: 2
