# List is a data type that allows multiple values and can be of different data types!
values = [1, 2, "rahul", 4, 5.1]
print(values[0])
print(values[4])
print(values[-1])
print(values[1:3])
values.insert(3, "shetty")
print(values)
values.append("End")
values[2] = "RAHUL"         # This replaces the third value as opposed to inserting a new one like in l.7!
del values[0]

print(values)


# Tuples can't be modified!
val = (1, 2, "rahul", 4.5)

print("\nThe following is a dictionary!")
# Dictionary
dic = {"a": 2, 4: "bcd", "c": "Hello World!"}

print(dic[4])
print(dic["c"])