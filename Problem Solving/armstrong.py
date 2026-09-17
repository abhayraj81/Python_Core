import math

n = input("Enter a Number: ")

a = len(n)
num = int(n)
s = 0

for i in n:
    s += pow(int(i), a)

if s == num:
    print("Yes")
else:
    print("No")