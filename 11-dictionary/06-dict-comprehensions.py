#   Dictionary Comprehension

# allows to create dictionary in concise way.

# syntax :
# new_dict = {key_expression: vlaue_expression for item in iterable if condition}

my_dict = {x : x*x for x in range (1,6)}
print(my_dict)

my_dict = {x : x+x for x in range (1,6)}
print(my_dict)
