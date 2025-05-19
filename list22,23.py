"""Python Lists
Lists are ordered collection of data items.
They store multiple items in a single variable.
List items are separated by commas and enclosed within square brackets [].
Lists are changeable meaning we can alter them after creation."""
details = ["Abhijeet", 18, "FYBScIT", 9.8]
print(details)
for i in range(len(details)):
    print(details[i],end=" ")
print()
print(details[-1])  # last element
print(details[0:3:2])  # slicing
#Check whether an item in present in the list?
if "Abhijeet" in details:
    print("Yes, 'Abhijeet' is present in the list")
else:
    print("No, 'Abhijeet' is not present in the list")
#List comprehension
#List comprehension is a concise way to create lists.
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)


#List methods
lst=[4,5,6,7,6,8,9]
print(lst)
lst.append(1)#add 1 to the end of the list
print(lst)
lst.insert(2,2)#insert 2 at index 2
print(lst)
print(lst.sort())
lst.remove(7)#remove 3 from the list
print(lst)
print(lst.index(6))#first occurrence of 6   
print(lst.count(6))#count of 6
print(lst.pop())#remove last element
print(lst)
newlst=lst.copy()#copy the list
lst.clear()#remove all elements
print(lst)
print(newlst)
#add a list to a list
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)
colors.reverse()#reverse the list
print(colors)
print(newlst+colors)#concatenate two lists

