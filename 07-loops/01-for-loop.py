# for loop

lang = "Python"
for x in lang:
    print(x)

print("_______________________________\n")

lang1  = ["Python","Java","Cobol"]
for x in lang1:
    print(x)

print("_______________________________\n")

# range(start , stop , step )
# range(stop)

for i in range (5): # by default start from 0
    print(i)
    
print("_______________________________\n")

for i in range(5,10): # with start , stop argument
    print(i)

print("_______________________________\n")

for i in range (1,10,2): # with start , stop , step argument
    print(i)

print("_______________________________\n")

for i in range (5):
    print(i)
else:
    print("for loop ended")

