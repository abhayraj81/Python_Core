# WAP to determine given year is leap year or not

y = int(input("Enter Year"))
if (y%4 == 0 and y%100 !=0) or y%400 ==0:
    print(f"{y} is Leap Year")
else :
    print(f"{y} is not Leap Year")
    

