class Person:
    name="Suraj"
    age=19
    #A constructor is a unique function that gets called automatically when an object is created of a class. The main purpose of a constructor is to initialize or assign values to the data members of that class. It cannot return any value other than None.
    def __init__(self):
        print("Default Constructor is called")
    #self parameter is a reference to the current instance of the class
    def info(self):
        print("Name is",self.name)
        print("Age is",self.age)
obj1=Person()#instantitation of class  Default constructor is called
#obj1 is an object of class Person
obj1.name="Mohan"
obj1.age=20
obj1.info()
print(obj1.__init__())#None


# Parametreized constructor
class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("Parametreized constructor is called")
    def info(self):
        print("Name is",self.name)
        print("Age is",self.age)
obj2=Employee("Sohan",24)#instantitation of class  Parametreized constructor is called
obj2.info()