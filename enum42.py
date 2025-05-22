'''The enumerate function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time.
 It returns an iterator that produces pairs of index and value for each element in the sequence. The enumerate function is often used in for loops to simplify the process of iterating over a sequence while keeping track of the index.
The enumerate function takes two arguments: the sequence to be enumerated and an optional start index. The start index specifies the value of the first index in the enumeration. If not provided, the default start index is 0.'''
# Loop over a list and print the index and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits,start=2):
    print(index, fruit)
print(enumerate.__doc__)
print(enumerate(fruits))
print(list(enumerate(fruits)))
print(*enumerate(fruits))