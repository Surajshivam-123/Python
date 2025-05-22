a = None
b = None

print(a is b) # exact location of object in memory true
print(a is None) # exact location of object in memory true
print(a == b) # true

x=[1,2,3]
y=[1,2,3]
print(x==y)# true
print(x is y) # false
#In this case, a and b are two separate lists that have the same values
#However, a and b are not the same object in memory, so is returns False

#in Python, strings and integers are immutable, which means that once they are created, their value cannot be changed. This means that, for strings and integers, is and == will always return the same result
a = "hello"
b = "hello"

print(a == b)  # True
print(a is b)  # True

a = 5
b = 5

print(a == b)  # True
print(a is b)  # True