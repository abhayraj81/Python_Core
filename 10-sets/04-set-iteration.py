#   Set iterations


numbers = {1,2,3,4,5}

#using for loop
for i in numbers:
    print(i)

print("\n---------------------------\n")

#   While loop
#   first convert set into list then use while loop coz set doesn't support indexing
numbersNew = list(numbers)

index = 0
while index < len(numbersNew):
    print (numbersNew[index])
    index += 1