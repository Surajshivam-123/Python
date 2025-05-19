'''Tuples are ordered collection of data items.
 They store multiple items in a single variable.
 Tuple items are separated by commas and enclosed within round brackets (). Tuples are unchangeable meaning we can not alter them after creation.'''
tuple1 = (1,2,2,3,5,4,6)
tuple2 = ("Red", "Green", "Blue")
details = ("Abhijeet", 18, "FYBScIT", 9.8)
print(type(tuple1))  # type of tuple
#print(tuple1[18])out of range
print(tuple1)
print(tuple2)
print(details)
print(tuple1[0])  # first element
print(tuple1[-1])  # last element
print(tuple1[0:3:2])  # slicing
# Check whether an item in present in the tuple?
if "Abhijeet" in details:
    print("Yes, 'Abhijeet' is present in the tuple")
else:
    print("No, 'Abhijeet' is not present in the tuple")
#If you want to add, remove or change tuple items, then first you must convert the tuple to a list.
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)# convert tuple to list
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)# convert list to tuple
print(countries)
print(countries+tuple1)  # concatenation
#Tuple methods
#As tuple is immutable type of collection of elements it have limited built in methods.They are explained below.
print(tuple1.count(2))
print(tuple1.index(2))  # index of first occurrence of 2
#Tuple packing and unpacking
#Packing
#Packing is the process of assigning multiple values to a single variable.
#Unpacking
#Unpacking is the process of extracting values from a tuple and assigning them to multiple variables.
#Example of packing and unpacking
#Packing
a = (1, 2, 3, 4, 5)
b = (6, 7, 8, 9, 10)
c = (11, 12, 13, 14, 15)
d = (16, 17, 18, 19, 20)
#Unpacking
a1, a2, a3, a4, a5 = a
b1, b2, b3, b4, b5 = b
c1, c2, c3, c4, c5 = c
d1, d2, d3, d4, d5 = d
print(a1, a2, a3, a4, a5)
print(b1, b2, b3, b4, b5)
print(c1, c2, c3, c4, c5)
print(d1, d2, d3, d4, d5)
#Tuple with single element
#To create a tuple with a single element, you need to add a comma after the element.
single_element_tuple = (1,)
