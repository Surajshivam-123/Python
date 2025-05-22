#openining a file
f=open("file.txt")
'''There are various modes in which we can open files.

read (r): This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter.

write (w): This mode opens the file for writing only and creates a new file if the file does not exist.

append (a): This mode opens the file for appending only and creates a new file if the file does not exist.

create (x): This mode creates a file and gives an error if the file already exists.

text (t): Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files. t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default. The default mode is 'r' (open for reading text, synonym of 'rt' ).

binary (b): used to handle binary files (images, pdfs, etc)'''

#reading a file
f=open("file.txt","r")
print(f.read())
#reading a file line by line
print(f.readline()) #reads the first line
print(f.readline()) #reads the second line

#reading a file line by line using for loop
for line in f:
    print(line)

#writing to a file
f=open("file.txt","w")
f.write("This is a new line\n")
f.write("This is another new line\n")
#The writelines() method in Python writes a sequence of strings to a file. The sequence can be any iterable object, such as a list or a tuple.
f.writelines(["This is a new line\n", "This is another new line\n"])
#appending to a file
f=open("file.txt","a")
f.write("This is an appended line\n")
#using with statement to open a file
#with open("file.txt","r") as f:
#    print(f.read())
#no need to close the file explicitly as it is done automatically
f.truncate(40) #truncates the file to 40 bytes
f=open("file.txt","r")
print("Seeking a file")
#seeking a file
f.seek(5)
print(f.read())
f.seek(20)
print("Tell the pointer",f.tell())