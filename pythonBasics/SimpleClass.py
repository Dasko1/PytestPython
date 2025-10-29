# This is the first part of the OopsDemo.py before going on to Constructors, et al.

class Calculator:
    num = 100               # Class variable; these are constant, ie, static!

    # Default constructor; you don't have to create a default constructor!  It exists!
    def __init__(self):
        print("I am called automatically when the object is created!")

    def getData(self):
        print("I am now executing as a method in class Calculator!")


obj = Calculator()          # Syntax to create objects in Python!
obj.getData()
print(obj.num)


# Class variable: these are defined in the class, like num = 100
# Instance variable: these are created in the constructor!
# (self) is mandatory when you declare a method inside a class!