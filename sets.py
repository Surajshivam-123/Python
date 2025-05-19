'''
Sets are unordered collection of data items. 
They store multiple items in a single variable.
Set items are separated by commas and enclosed within curly brackets {}.
Sets are unchangeable, meaning you cannot change items of the set once created. Sets do not contain duplicate items.
they cannot be accessed using index numbers
'''
info = {"Carla", 19, False, 5.9, 19}
print(info)
st=set()
print(type(st))
#Accessing set items:
info = {"Carla", 19, False, 5.9}
for item in info:
    print(item)
num={3,1,5,2,4}
print(num)#sorted(num))
#Adding items to a set:
num.add(6)
print(num)

#Joining two sets:
print("Union of two sets:")
#I. union() and update():
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
print(cities3)
print(cities | cities2)
print(cities)
print(cities2)
cities.update(cities2)
print(cities)

print("Intersection of two sets:")
#II. intersection() and intersection_update():
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)
print(cities & cities2)
print(cities)
print(cities2)
cities.intersection_update(cities2)
print(cities)

print("Symmetric Difference of two sets:")
#III. symmetric_difference and symmetric_difference_update():
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)
print(cities ^ cities2)
print(cities)
print(cities2)
cities.symmetric_difference_update(cities2)
print(cities)

print("Difference of two sets:")
#IV. difference() and difference_update():
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.difference(cities2)
print(cities3)
print(cities - cities2)
print(cities)
print(cities2)
cities.difference_update(cities2)
print(cities)

print("Discarding an item from a set:")
#V. discard() and remove():
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.discard("Tokyo")
print(cities)
cities.remove("Madrid")
print(cities)
#cities.remove("Tokyo")#will raise an error
#cities.discard("Tokyo")#will not raise an error

print("Clearing a set:")
#VI. clear():
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)

print("Copying a set:")
#VII. copy():
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = cities.copy()
print(cities2)

print("Set Comprehension:")
#VIII. set comprehension:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {city for city in cities if "o" in city}
print(cities2)

print("Frozen Set:")
#IX. frozenset():
#A frozenset is a built-in set in Python that is immutable, meaning it cannot be changed after creation.
#It is similar to a regular set, but it cannot be modified.
#Frozensets are hashable, meaning they can be used as keys in dictionaries or elements in other sets.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = frozenset(cities)
print(cities2)
print(type(cities2))

print("Set Methods:")
#X. set methods:
print("Isdisjoint:")
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))

print("Issubset:")
cities = {"Tokyo", "Madrid"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid", "Berlin", "Delhi"}
print(cities.issubset(cities2))

print("Issuperset:")
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Madrid"}
print(cities.issuperset(cities2))

print("Pop:")
#XI. pop():
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
print(cities.pop())
#The pop() method removes and returns an arbitrary element from the set.
#Note: The pop() method does not take any arguments and does not raise an error if the set is empty.
#The pop() method is useful when you want to remove an arbitrary element from the set without knowing its value.
#The pop() method is not guaranteed to remove the same element every time, as sets are unordered collections.

print("Set Length:")
#XII. len():
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
print(len(cities))
#The len() function returns the number of elements in the set.

print("Adding an item to a set:")
#XIII. add():
cities.add("Pune")
print(cities)

print("delete")
del cities
print(cities)

