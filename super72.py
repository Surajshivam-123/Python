#The super() keyword in Python is used to refer to the parent class. It is especially useful when a class inherits from multiple parent classes and you want to call a method from one of the parent classes.
class ParentClass1:
    def parent_method(self):
        print("This is the parent method from parentclass1.")
class ParentClass2:
    def parent_method(self):
        print("This is another parent method from Parentclass2.")
    def another_method(self):
        print("This is another method from ParentClass2.")
class ChildClass(ParentClass1,ParentClass2):
    def parent_method(self):
        print("This is the overridden parent method.")
    def child_method(self):
        print("This is the child method.")
        super().parent_method()
# Create an instance of ChildClass and call its methods

child_object = ChildClass()
child_object.child_method()
child_object.parent_method()

class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id

class Programmer(Employee):
  def __init__(self, name, id, lang):
    super().__init__( name, id)
    self.lang = lang

rohan = Employee("Rohan Das", "420")
harry = Programmer("Harry", "2345", "Python")
print(harry.name)
print(harry.id)
print(harry.lang)
