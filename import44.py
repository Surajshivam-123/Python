#import math
from math import sqrt
result = sqrt(9)
print(result)  # Output: 3.0
from math import pi
print(pi)
import math
print(math.pi)

#import everything
from math import *

result = sqrt(9)
print(result)  # Output: 3.0

print(pi)  # Output: 3.141592653589793

#aliasing
import math as m
result = m.sqrt(9)
print(result)  # Output: 3.0

#list all functions and variables in the math module in the form of a list
print(dir(math))

import helper
helper.welcome()
