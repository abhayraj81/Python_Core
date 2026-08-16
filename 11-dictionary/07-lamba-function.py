# Lambda function in python

# > uses keyword lambda
# > can have number of argument but only in one  expression

# syntax :  lambda arguments : expression
#         > Arguments : input to the function
#         > Expression : A single statement or operation that the lambda function .  

# add two numbers using lambda fucntion
add = lambda x,y : x + y
print(add(3,5))

# custom sorting - sort a list of tuples by the second element
data = [(1,'b'),(3,'a'),(2,'c')]
sorted_data = sorted(data, key = lambda x: x[0])
print(sorted_data)

sorted_data = sorted(data, key = lambda x: x[1])
print(sorted_data)

