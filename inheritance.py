class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id 

  def showDetails(self):
    print(f"The name of Employee: {self.id} is {self.name}")

class Programmer(Employee):
  def showLanguage(self):
    print("The default langauge is Python")


e1 = Employee("Rohan Das", 400)
e1.showDetails()
e2 = Programmer("Harry", 4100)
e2.showDetails()
e2.showLanguage()
#Types of inheritance:
"""
Single inheritance
Multiple inheritance
Multilevel inheritance
Hierarchical Inheritance
Hybrid Inheritance
"""

print("Single Inheritance")
#single inheritance
class Person:
  def __init__(self,name):
    print("Person constructor")
    self.name=name
  def same(self):
     print("Person class method")
  def show(self):
    print("Name is",self.name)
class Student(Person):
  def __init__(self,name,rollno):
    print("Student constructor")
    Person.__init__(self,name)
    self.roolno=rollno
  def same(self):
    print("Student class method")
  def shows(self):
    #Person.show(self)
    super().show()#this also works
    print("Roll no is",self.roolno)
s1=Student("Rohan",101)
s1.show()#inherited from Person
s1.shows()#from Student
s1.same()
print(Student.mro())
p=Person("Ravi")
p.same()

print("Multiple Inheritance")
#Multiple inheritance
class A:
  def __init__(self,value):
    print("A constructor")
    self.valueA=value
  def showA(self):
    print("Value of A is",self.valueA)
class B:
  def __init__(self,value):
    print("B constructor")
    self.valueB=value
  def showB(self):
    print("Value of B is",self.valueB)
class C(A,B):
    def __init__(self,valueA,valueB):
        print("C constructor")
        """self.valueA=valueA
        self.valueB=valueB"""
        #A.__init__(self,valueA)
        #B.__init__(self,valueB)
        super().__init__(valueB)
        super(A,self).__init__(valueA)
        self.valueC=valueA+valueB
    def showC(self):
        print("Value of C is",self.valueA+self.valueB)
c1=C(10,20)
c1.showA()
c1.showB()
c1.showC()
print(C.mro())

#use of super() in multiple inheritance
class A:
    def __init__(self):
        print("A's constructor")
        
class B(A):
    def __init__(self):
        super().__init__()
        print("B's constructor")
        
class C(A):
    def __init__(self):
        super().__init__()
        print("C's constructor")

class D(B, C):  # Multiple inheritance
    def __init__(self):
        super().__init__()  # Will call B, C, and A in correct order
        print("D's constructor")

d = D()

print("Multilevel Inheritance")
#Multilevel Inheritance :
class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername
class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        Grandfather.__init__(self, grandfathername)
class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        super().__init__(fathername, grandfathername)#without using Father.__init__(self,fathername, grandfathername)
 
    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)
s1 = Son('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
s1.print_name()
print(Son.mro())

print("Hierarchical Inheritance")
#Hierarchical Inheritance:
class Parent:
    def __init__(self):
       print("This is parent class constructor")
    def func1(self):
        print("This function is in parent class.")

class Child1(Parent):
    def __init__(self):
       print("This is child1 class constructor")
    def func2(self):
        print("This function is in child 1.")
      
class Child2(Parent):
    def __init__(self):
        print("This is child2 class constructor")
    def func3(self):
        print("This function is in child 2.")
 
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()

print("Hybrid Inheritance")
#Hybrid Inheritance:
class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def show_details(self):
    print("Name:", self.name)
    print("Age:", self.age)
    
class Person(Human):
  def __init__(self, name, age, address):
    Human.__init__(self, name, age)
    self.address = address
    
  def show_details(self):
    Human.show_details(self)
    print("Address:", self.address)
    
class Program:
  def __init__(self, program_name, duration):
    self.program_name = program_name
    self.duration = duration
    
  def show_details(self):
    print("Program Name:", self.program_name)
    print("Duration:", self.duration)
    
class Student(Person):
  def __init__(self, name, age, address, program):
    Person.__init__(self, name, age, address)
    self.program = program
    
  def show_details(self):
    Person.show_details(self)
    self.program.show_details()
program = Program("Computer Science", 4)
student = Student("John Doe", 25, "123 Main St.", program)
student.show_details()