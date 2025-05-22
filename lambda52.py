def add(x,y):
    return x+y
sub=lambda x,y:x-y
print(add(2,3))
print(sub(5,2))
def appl(fx, value):
  return 6 + fx(value)

print(appl(lambda x:x*x, 5))
msg=lambda :print("Good Evening")
msg()