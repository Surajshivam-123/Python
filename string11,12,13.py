# anything that you enclose between single or double quotation marks is considered a string.
#unicode characters are also strings.
print(u'\u01B4')  # In Python 2
print('\U000001B4')  # In Python 3
#Sometimes, the user might need to put quotation marks in between the strings. Example:
print("He said, 'I want to eat an apple'.")#OR
print('He said, "I want to eat an apple".')
#Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#Accessing Characters of a String
print(a[0])  # First character

#Looping through the string
for ch in a:
    print(ch, end=' ')
name="Suraj"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5]) # Throws an error

#String Slicing & Operations on String
#Length of a String
print(len(name))  # Length of the string
#Slicing
print(name[0:2])  # First two characters
print(name[2:])  # From the third character to the end
print(name[:3])  # From the beginning to the third character
print(name[1:4])  # From the second to the fourth character
print(name[-1])  # Last character
print(name[-2])  # Second last character
print(name[-3:])  # From the third last character to the end
print(name[:-1])  # From the beginning to the second last character
print(name[-2:-1])  # From the second last to the last character
print(name[-2:])  # From the second last character to the end
print("3",name[-1:-3])  # From the last to the second last character Not happens
#Loop through a String:
for i in name:
    print(i, end=' ')
print()
#String methods
str1 = "   AbcDEfghIJ   "
print(str1.upper())
print(str1.lower())
print(str1.title())
print(str1.capitalize())
print(str1.swapcase())
print(str1.strip())  # Removes leading and trailing spaces
print(str1.lstrip())  # Removes leading spaces
print(str1.rstrip())  # Removes trailing spaces
print(str1.replace("Abc", "xyz"))  # Replaces all spaces with empty string
print(str1.split())  # Splits the string into a list of words
print(str1.split(" "))  # Splits the string into a list of words
str1 = "Welcome to the Console!!!"
print(str1.center(50))  # Center the string in a field of 50 characters
print(str1.ljust(50))  # Left justify the string in a field of 50 characters
print(str1.rjust(50))  # Right justify the string in a field of 50 characters
print(str1.count("o"))  # Count the number of occurrences of "o" in the string
print(str1.find("o"))  # Find the first occurrence of "o" in the string
print(str1.rfind("o"))  # Find the last occurrence of "o" in the string
print(str1.index("o"))  # Find the first occurrence of "o" in the string
print(str1.rindex("o"))  # Find the last occurrence of "o" in the string
#The major difference being that index() raises an exception if value is absent whereas find()(return -1) does not.
print(str1.startswith("Welcome"))  # Check if the string starts with "Welcome"
print(str1.endswith("!!!"))  # Check if the string ends with "!!!"
print(str1.endswith("to", 4, 10))
print(str1.isalnum())  # Check if the string is alphanumeric
print(str1.isalpha())  # Check if the string is alphabetic
print(str1.isdigit())  # Check if the string is numeric
print(str1.islower())  # Check if the string is lowercase
print(str1.isupper())  # Check if the string is uppercase
print(str1.isspace())  # Check if the string is whitespace
 # Check if the string is printable
text = 'Hello World!'
print(text.isprintable())  # Output: True

text = 'Hello World!\n'
print(text.isprintable())  # Output: False 
# Check if the string is a title
text = 'Hello World!'
print(text.istitle())  # Output: True
text = 'Hello world!'
print(text.istitle())  # Output: False
# Check if the string is a valid identifier
text = 'my_variable'
print(text.isidentifier())  # Output: True
text = 'my variable'
print(text.isidentifier())  # Output: False

#delete
#del name[0]  # Throws an error
#del name  # Deletes the variable name
#del name[:]  # Deletes the entire string
#del name[0:1]  # Deletes the first character

#reverse the string
name = "Suraj"
print(name[::-1])  # Reverse the string
