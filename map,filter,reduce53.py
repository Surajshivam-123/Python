number=(1,2,3,4,5,6)
#THese are high order function which takes function as input
#map-The function argument is a function that is applied to each element in the iterable argument.
print(tuple(map(lambda x:x*x,number)))

#filter-The function argument is a function that returns True or False, and the iterable argument is filtered based on this function.
print(tuple(filter(lambda x:x%2==0,number)))

#reduce-The function argument is a function that takes two arguments and returns a single value, and the iterable argument is reduced to a single value using this function.
from functools import reduce
print(reduce(lambda x,y:x+y,number))

