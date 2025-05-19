'''try….. except blocks are used in python to handle errors and exceptions.
 The code in try block runs when there is no error.
   If the try block catches the error, then the except block is executed.
   '''
try:
    # code that may cause an error
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ValueError:
    # code that runs if there is a ValueError
    print("Invalid input! Please enter a valid number.")
except ZeroDivisionError:
    # code that runs if there is a ZeroDivisionError
    print("Error! Division by zero is not allowed.")
except IndexError:
    # code that runs if there is an IndexError
    print("Index out of range! Please check your list index.")
except TypeError:
    # code that runs if there is a TypeError
    print("Type error! Please check the data types.")
except KeyError:
    # code that runs if there is a KeyError
    print("Key error! Please check the dictionary key.")
except FileNotFoundError:
    # code that runs if there is a FileNotFoundError
    print("File not found! Please check the file path.")
except Exception as e:
    # code that runs for any other exception
    print("An unexpected error occurred:", str(e))
finally:
    # code that runs no matter what
    print("Execution completed.")
# The finally block is optional and can be used to execute code that should run regardless of whether an exception occurred or not.
# The try block is used to wrap the code that may cause an exception.
# The except block is used to handle specific exceptions that may occur.
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:# else block is executed if no exception occurs
    print("Integer Accepted.")
finally:
    print("This block is always executed.")