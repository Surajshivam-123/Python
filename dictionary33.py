''''Dictionaries are ordered collection of data items.
They store multiple items in a single variable.
Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.
Dictionaries are mutable, meaning they can be changed.
Dictionaries are indexed by keys, which can be of any immutable type (strings, numbers, tuples).
'''
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
#Accessing Dictionary items:
print(info['name'])
print(info.get('eligible'))
print(info.keys())#returns all keys in the dictionary in the form of a list
print(info.values())#returns all values in the dictionary in the form of a list
#access all key value pairs in the form of list of tuples
print(info.items())

#Dictionary methods
print("copy")
info2=info.copy()#returns a shallow copy of the dictionary
info['age']=20#updating the value of key 'age'
print(info)
print(info2)

print("clear")
info.clear()#removes all items from the dictionary
print(info)

print("update")
info2.update({'name':'Karan Singh'})#updates the value of key 'name' in info2
info2.update({'gender':'male'})#adds a
print(info2)

print("pop name")
info2.pop('name')#removes the key 'name' from the dictionary
print(info2)

print("popitem")
info2.popitem()#removes the last inserted key-value pair from the dictionary
print(info2)

print("setdefault")
info2.setdefault('name','Karan Singh')#if the key 'name' is not present in the dictionary, it will add the key-value pair to the dictionary
print(info2)

print("fromkeys")
info3=dict.fromkeys(['name','age'])#creates a new dictionary with the specified keys and assigns the value None to all keys
print(info3)

print("fromkeys with value")
info4=dict.fromkeys(['name','age'],0)#creates a new dictionary with the specified keys and assigns the value 0 to all keys
print(info4)

print("del")
del info2['name']#removes the key 'name' from the dictionary
print(info2)

print("del info2")
del info2#deletes the dictionary
# print(info2)#will give error as info2 is deleted