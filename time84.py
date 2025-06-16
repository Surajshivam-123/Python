import time
#The time.time() function returns the current time as a floating-point number, representing the number of seconds since the epoch (the point in time when the time module was initialized). 
print(time.time())

#The time.sleep() function suspends the execution of the current thread for a specified number of seconds.
print("Start:", time.time())
time.sleep(2)
print("End:", time.time())

#The time.strftime() function formats a time value as a string, based on a specified format
print("Current time:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))