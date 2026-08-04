# operators

# 1. Airthmetic Operators
a = 5
b = 3
print(a + b)  # addition operator
print(a - b)  # substractin operator
print(a * b)  # multiplication operator
print(a % b)  # modulus operator


# 2. Comparison Operators - output is boolean
a = 5
b = 3
print(a > b)  # greater operator
print(a < b)  # lessthan operator
b = 5
print(a == b)  # equal to operator
print(a != b)  # equal to operator


# 3. Assignment Operator
a = 5 #here = is assignment operator


# 4. Logical Operator
# Rule for 'and' operator
#      True + True = True
#      True + False = False
#      False + True = False
#      False+ False = False
a = 10
b = 20
print(a>10 and b<10)
print(a==10 and b==20)
# or operator
# Rule for 'or' operator
#      True + True = True
#      True + False = True
#      False + True = True
#      False+ False = False
print(a==10 or b<10) 
# not operator
print(not(a==10 and b==20))


# 5. identity operator 'is' 'is not' (compare memory location)
x = [1,2,3]
y = x
z = [1,2,3]
print(x is y) # is operator
print(x is z)
print(x is not z) # is not operator

# 6. membership operators 'in' 'not in'
my_list = ['apple','orange','watermelon']
print('apple' in my_list) # in operator
print('apple2' in my_list)
print('apple2' not in my_list)  #not in operator


# 7. bitwise operator - &, |, ^, `, etc
a = 5            # 5 in binary - 0101 
b = 3            # 3 in binary - 0011
print(a & b)     # 1 in binary - 0001

a = 5            # 5 in binary - 0101 
b = 3            # 3 in binary - 0011
print(a | b)     # 7 in binary - 0111

a = 5            # 5 in binary - 0101 
b = 3            # 3 in binary - 0011
print(a ^ b)     # 6 in binary - 0110

a = 5            # 5 in binary - 0101 
b = 3            # 3 in binary - 0011
# ~a adds 1 bit from right to binary of 5 ie 0101 + 1 = 0111
print(~a)        # 6 in binary - 0110




