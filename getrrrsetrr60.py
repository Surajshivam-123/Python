class Details:
    def __init__(self,value):
        self._value=value
    #The value method is defined as a getter using the @property decorator, and is used to return the value of the _value property.
    @property
    def valuelox(self):
        return 10*self._value
    #The setter method is defined using the @value.setter decorator, and is used to set the value of the _value property.
    @valuelox.setter#@property_name.setter
    def value(self,new_value):
        self._value=new_value/10
obj1=Details(10)
print(obj1._value)
print(obj1.valuelox)# now we can access the value property using the getter method.
#getters do not take any parameters and we cannot set the value through getter method.
obj1.value=20# we can set the value using the setter method.
print(obj1.valuelox)
print(obj1._value)