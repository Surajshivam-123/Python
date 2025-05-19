#we can raise custom errors by using the raise keyword.
salary = int(input("Enter salary amount: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")

#In Python, we can define custom exceptions by creating a new class that is derived from the built-in Exception class.
class SalaryError(Exception):
    pass
try:
    salary = int(input("Enter salary amount: "))
    if not 2000 < salary < 5000:
        raise SalaryError("Not a valid salary")
except SalaryError as e:
    print(e)