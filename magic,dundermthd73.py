from helper import Employee
emp=Employee("John")
print(len(emp))
print(emp)
print(dir(emp))
#The str and repr methods are both used to convert an object to a string representation.
print(str(emp))
print(repr(emp))
#This is an incredibly powerful tool that allows you to create objects that behave like functions.
print(emp())