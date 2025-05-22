#class method-A class method is a type of method that is bound to the class and not the instance of the class.
#  In other words, it operates on the class as a whole, rather than on a specific instance of the class.
#  Class methods are defined using the "@classmethod" decorator, followed by a function definition.
#  The first argument of the function is always "cls," which represents the class itself.

'''Use  of Python Class Methods'''
class Employee:
    # Class variable
    company = "TechCorp"

    # Constructor
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def changeCompany(cls, new_company):
        cls.company = new_company
    # Class method to change the company name
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    # Instance method to display employee details
    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Company: {self.company}")
e1= Employee("Alice", 50000)
e1.display()
print(Employee.company) 
e1.changeCompany("NewTech")
e1.display()
print(Employee.company) 

e1.change_company("GlobalTech")
e1.display()
print(Employee.company)

#to create a factory method that creates instances of your class in a specific way
class Employee:
    # Class variable
    company = "TechCorp"
    # Constructor
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Class method to create an employee with a default salary
    @classmethod
    def create_with_default_salary(cls, name):
        return cls(name, 30000)  # Default salary is set to 30000
    
#define a class method that creates the instance and returns it to the caller
    @classmethod
    def create_employee(cls, name, salary):
        return cls(name, salary)
    
    # Instance method to display employee details
    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Company: {self.company}")

#to provide alternative constructors for your class.
e2 = Employee.create_with_default_salary("Bob")
e2.display()
e3 = Employee.create_employee("Charlie", 40000)
e3.display()

class Person:
    def __init__(self, name, age):#defalut constructor
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))
p=Person.from_string("Sred,23")
print(p.name, p.age)