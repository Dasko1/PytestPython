# Use GetName as a class from which you can inherit!

class GetName:

    def __init__(self):
        self.yourName = input("Enter a name: ")

    def returnName(self):
        return self.yourName


obj = GetName()
print("\nThe name is: ", obj.returnName())
