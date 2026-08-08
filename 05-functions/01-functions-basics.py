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


# 2. Function with Return Statement

def add(a,b):
    return(a+b) # this line sends back sum of a add
    return(a-b) # after first return statement function ends.
result = add(56,4)
print(result)

# function to convert celcius to fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) +32
    return fahrenheit
# call a function
temp_f1 = celsius_to_fahrenheit(25)
print(temp_f1)
print("With return statement : ", type(temp_f1))

# function without return statement
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) +32
    print(fahrenheit)
# call a function
temp_f2 = celsius_to_fahrenheit(50)
print(temp_f2)
print("Without return statement : " , type(temp_f2))

# 3. Pass Statement
def anything():
    pass # code to be updated Later
print(" Yep ! Gotcha")

