file = open('test.txt')
# Read all the contents of a file!
# print(file.read())
# print(file.readline())


# Print line by line using readLine method.
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()


values = ['aardvark', 'bear', 'cat', 'dog', 'elephant']
for line in file.readlines():
    print(line)


file.close()