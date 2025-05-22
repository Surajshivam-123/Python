def welcome():
    print("Welcome to the Python Quiz!")
    print("You will be asked a series of questions.")
    print("Please answer with the letter corresponding to your choice.")
    print("Good luck!\n")
print(__name__)
if __name__ == "__main__":
    welcome()
    # Add any additional code you want to run when this module is executed directly
    # For example, you can call the welcome function here
    # welcome()
class Employee:
    def __init__(self,name):
        self.name=name
    def __len__(self):
        ans=0
        for i in self.name:
            ans+=1
        return ans

    def __str__(self):
        return f"My name is {self.name}"
    def __repr__(self):#if str is not defined then repr is used
        return f"Employee({self.name})"
    def __call__(self):
        return f"Hello {self.name}"

