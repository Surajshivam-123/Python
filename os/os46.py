'''The os module in Python is a built-in library that provides functions for interacting with the operating system. It allows you to perform a wide variety of tasks, such as reading and writing files, interacting with the file system, and running system commands.'''
import os
f=open('myfile.txt','w')
f.write('Hello World')
f.close()
# Open the file in read mode
f1=os.open('myfile.txt',os.O_RDONLY)
print('File descriptor:',f1)
str=os.read(f1,5)
print('Read string:',str)
os.close(f1)
f2=os.open('myfile.txt',os.O_WRONLY)
os.write(f2,b"\nWelcome to Python")
os.close(f2)
# Close the file descriptor
# The os module provides a way to interact with the operating system in a platform-independent manner.
# It allows you to perform tasks such as file and directory manipulation, process management, and environment variable access.
# The os module is part of the Python standard library, so you don't need to install it separately.
# The os module is a powerful tool for working with the operating system in Python.

#to get a list of the files in a directory:
files=os.listdir('.')
print('Files in the current directory:',files)

#to create a new directory:
os.mkdir('new_directory')

#to remove a directory:
os.rmdir('new_directory')

#Running system commands
file=os.system('ls')
print(file)
# Run the "ls" command and get the output as a file-like object
print(os.popen('ls').read())