# conditional statement in python

# 1. if statement
a = 26
b = 108
if b > a:
    print("b is greater than a")

a = int(input("Enter Your Age : "))
if a > 19:
    print("You are Adult")

# 2. if-else condition
a = int(input("Enter Your Age : "))
if a > 19:
    print("You are Adult")
else:
    print("under age")

# 3. if-elif-else condition
# multiple condition
score = int(input("Enter Score : "))
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else :
    print("Grade D")

# 4. Nested If-else Condition
# if-else block inside another if-else block
n = int(input("Enter Number : "))
if n > 0:
    if n%2 == 0 :
        print("Number is Even")
    else :
        print("Number is positive and Odd")
else:
    if n == 0 :
        print("the number is zero")
    else:
        print("Number is negative")

# 5. Conditional Statement (ternary statement)
a = int(input("Enter Age"))
status = "Adult" if a >= 18 else "minor"
print(status)
