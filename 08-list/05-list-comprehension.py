# List Comprehensions

# syntax :
# list-name = [ expression for item in iterable if condition]

# create a list of square
squares = [x**2 for x in range(1,6)]
print(squares)

# filter even numbers
evenList = [x for x in range(1,11) if x % 2 == 0]
print(evenList)

# apply function to element of a list
my_list = ["apple","mango","cherry"]
uppercase_list = [lst.upper() for lst in my_list]
print(uppercase_list)

# flatten a nested list using list comprehension
nested_list = [[1,2], [3,4], [5,6]]

def flatten_list(lst):
    return [item for sublist in lst for item in sublist]

final_list = flatten_list(nested_list)
print(final_list)

