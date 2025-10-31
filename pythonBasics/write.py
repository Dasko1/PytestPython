# Read the file and store all the lines in list!
# Reverse the list & write the list back to the file!

# Reverse the order in test.txt!
with open('test.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    # Open the file again, this time in write mode!
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
