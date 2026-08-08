# String in Python
# Characters in single, double and triple quotes

name = "Abhay Raj"  # creating a string
print(name)
print(type(name))   # checking data type
print('Hello World')
print("It's easy")

# formatted Strings

# 1. old style formatting - % formatting
name = "Raj Abhay"
age = 23
print("my name is %s and i am %d ." %(name,age)) 
# %s and %d are the placeholder for string and int. 

# 2. str.format()
name = "Abhay"
age = 23
print("my name is {} and i am {}.".format(name,age)) 
# you can reference variables by index and keyword
print("my name is {0} and i am {1}.".format(name,age)) 
print("my name is {1} and i am {0}.".format(name,age))
print("my name is {0} and i am {0}.".format(name,age)) 
print("my name is {1} and i am {1}.".format(name,age))
# contains different format types

# 3. f-strings (formatted string literals)
name = "Abhay"
age = 23
print(f"my name is {name} and i am {age}")
print(f"my age is after 5 years will be {age+5}")

#----------------------------------------------------------------------

# Escape Character - backslash with character
print(" \"Abhay-Raj Quotes\" ")
print("Hello\nWorld!")      # new line
print("Hello\tWorld!")      # tab 