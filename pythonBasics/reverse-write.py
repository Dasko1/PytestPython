# Reverse the characters of a string!

ReverseThis = "Finland"
print("Reverse this: ", ReverseThis)

# Put the value in ReverseThis into a list!  You can print out each step of the process if you want!
x = ["Finland"]
# print(x)

# Separate the characters in ReverseThis value into separate list elements!
y = list(''.join(x))
# print(y)

# Reverse the separate elements stored in 'y'!
y.reverse()
# print(y)

# Join the reversed elements back into a string stored in z!
z = ''.join(y)
print("\nThe reversed word is: ", z)
