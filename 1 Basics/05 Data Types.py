# Data types in Python
a = 1
b = 2
print(a+b)
print(type(a+b))

c = "1"
d = "2"
print(c+d)
print(type(c+d))

# Basic data types in python

#1. Numeric
a1 = 1              #integer
a2 = 1.5            #float
print(a2)
print(type(a2))     
a3 = complex(3,5)   #complex
print(a3)
print(type(a3))


#2. Sequence
b1 = "Abhay Raj"        #String
print(b1)
print(type(b1))

b2 = [1,4,7,8,26,108,"Abhay"]   #List 
print(b2)
print(type(b2))

b3 = (1,4,7,8,26,108,"Abhay")   #tuple 
print(b3)
print(type(b3))


#3. Dictionary {'KEY':'Value'}
my_dictionary = {'name':'Abhay','age':23,'city':'kanpur'}
print(my_dictionary)
print(type(my_dictionary))

#4. Sets
my_sets = {1,4,7,8,26,108,"Abhay"}   #set
print(my_sets)
print(type(my_sets))


#5. Boolean
bool1 = True
bool2 = False
print(bool1)
print(bool2)
print(type(bool1))


#6. Binary
# bytes, bytearray, memoryview
byte1 = b"Abhay"
print(byte1)
print(type(byte1))