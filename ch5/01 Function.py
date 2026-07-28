# 1. Function without Parameters

# Create or Define a Function
def greetings():
    print("Welcome to India ! ")
# Use or Call this Function
greetings()

# 2. Function with Param

# create function to add two numbers
def add2nums(a,b):
    result=(a+b)
    print("Sum of two numbers are ",result)
# calling function with arguments
add2nums(56,88)
add2nums(a=6,b=9)
add2nums(b=23,a=1)

# create function to add two numbers
def add3nums(a,b,c):
    result=(a+b+c)
    print("Sum of three numbers are ",result)
# calling function
add3nums(6,5,8)
add3nums(a=9,b=33,c=2)
add3nums(b=23,a=1,c=90)


# 2. Return Statement
def add(a,b):
    return(a+b)
result = add(56,4)
print(result)
