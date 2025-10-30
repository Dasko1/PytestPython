# This class will inherit the properties from the parent class GetName!
# First, you have to import the parent class from the package pythonBasics!
# You don't need to create a constructor like in GetName because ImplementGetName (child class) inherits it from the parent GetName!
from pythonBasics import GetName


# Create a child class name and call the parent in parentheses!
class ImplementGetName(GetName):

    # Create a new method in the child class; "self" is a keyword that is mandatory for calling variable names into method!
    def getFirstName(self):
        return self.getFirstName()


# "obj" is a new class declaration from ImplementGetName; ImplementGetName is a child class getting the properties of the parent class GetName!
# Notice that you don't have to write a line for input, because that is in the GetName parent class ImplementGetName inherits!
# Remember in l.19 "obj" is the class & "getFirstName" is the method!
obj = ImplementGetName()
print(obj.getFirstName())