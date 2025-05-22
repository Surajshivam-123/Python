x=10
y=20
def changex():
    global x,z
    z=21
    x=30
def changey():
    x=50
    y=40
print("Before function call: x =", x, "y =", y)
changex()
print("After changex: x =", x, "y =", y)
changey()#Not global
# y is not changed
print("After changey: x =", x, "y =", y)
print("z=",z)