import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime

greet_time=int(time.strftime("%H"))
if(greet_time<12):
    print("Good Morning")
elif(greet_time<17):
    print("Good Afternoon")
elif(greet_time<20):
    print("Good Evening")
else:
    print("Good Night")