#For loop
#iterating over a string:
name = 'Abhishek'
for i in name:
    print(i, end=", ")
print()
 #iterating over a list:
lst=["suraj",5,True,3.14]
for i in lst:
    print(i, end=", ")
print()
#for a specific number of times
for i in range(5):
    print(i,end=", ")
print()
for i in range(4,10,2):
    print(i,end=", ")
print()

#while loop
count = 5
while (count > 0):
  print(count,end=" ")
  count = count - 1
#Else with While Loop
count=int(input("Enter a Number: "))
while (count > 0):
  print(count,end=" ")
  count = count - 1
else:
    print("Count is Zero")
print()
#emulate do while loop
while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break