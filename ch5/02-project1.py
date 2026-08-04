# WAP to make simple calculator using function performs atleast 5 operations

# creating functions for all operations
def add(a,b):
    return a+b
def sub(a,b):
    if a>b:
        return a-b
    else:
        return -(b-a)    
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def avg(a,b):
    av = (a+b)/2
    return av

# statement to choose operation
print("Please Select Operation : \n "\
      "1. 'add' for Addition \n"\
      "2. 'sub' for Substraction \n"\
      "3. 'mul' for Multiplication\n"\
      "4. 'div' for Division\n"\
      "5. 'av' for Average")
# taking input for from user
select = int((input("select a operation from 1 to 5 : ")))
a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
# conditions for user selection~
if select == 1:
    print(a," + ",b," = ",add(a,b))
elif select == 2:
    print(a," - ",b," = ",sub(a,b))
elif select == 3:
    print(a," * ",b," = ",mul(a,b))
elif select == 4:
    print(a," / ",b," = ",div(a,b))
elif select == 5:
    print("(",a," + ",b,")","/2"," = ",avg(a,b))
else:
    ("Invalid Input")

