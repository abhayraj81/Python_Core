# list in python

# Syntax : List_name = [element1, element2, element3,.........]

# 1. list of Strings
color = ["red","blue","green","yellow"]
print(type(color))

# 2. list of Integer
numbers = [5,65,8,4,54,1]
print(type(numbers))

# 3 . Mixed data types
mixed = ["hello", 1, 3.14, True]
print(type(mixed))

# 4. Nested List
nested = [1, [2,3], [4,5,6], ["o","p"]]
print(type(nested))


# Accessing element of list
# syntax : list_name[index]
print(color[0])
print(numbers[1])
print(mixed[2])
print(nested[3])
print(color[-1])
print(numbers[-2])
print(mixed[-3])
print(nested[-4])

