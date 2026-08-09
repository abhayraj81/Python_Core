# nested loop

# Syntax :-
# outer_loop:
#     inner_loop:
#         block of code for inner loop
# block of code for outer loop

# print number from 1 to 3 three times
for i in range(3):
    print("Outer loop iteration no, ",i)
    for num in range(1,4):
        print(num)
    print("- - -")

# using while and for loop
i = 1
while i < 4:
    print("while loop iteration no. : ",i)
    for j in range(1,4):
        print(j)
    #print("- - -")
    i += 1


# print prime number from 2 to 10 using nested loop
print("prime no.s between 2 to 10")
for num in range(2,10):    
    for i in range(2,num):
        if num % i == 0 :
            break
    else:
        print(num)



