#   SET Comprehensions

#   >> similar to list comprehensions
#   >> allows concise and readable creation of list

# syntax : 
# new_set = {expression for item in iterable if conditon}

squares = {x ** 2 for x in range (1,6)}
print(squares)

# Extract only even numbers greater than 10
numbers = [4, 11, 14, 22, 9, 14]
even_set = {num for num in numbers if num > 10 and num % 2 == 0}
print(even_set) 
