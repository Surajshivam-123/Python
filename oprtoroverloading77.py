class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    #overloading of +operator
    def __add__(self,other):
        return Point(self.x+other.x,self.y+other.y)
    def __lt__(self,other):
        return self.x**2 +self.y**2 < other.x**2 + other.y**2
    #You can overload an operator in Python by defining special methods in your class.
    #  These methods are identified by their names, which start and end with double underscores (__).
    #  Here are some of the most commonly overloaded operators and their corresponding special methods:
    ''' + : __add__
        - : __sub__
        * : __mul__
        / : __truediv__
        < : __lt__
        > : __gt__
        == : __eq__'''
p1=Point(2,3)
p2=Point(5,6)
p3=p1+p2
print(p3.x,p3.y)
print(p1<p2)