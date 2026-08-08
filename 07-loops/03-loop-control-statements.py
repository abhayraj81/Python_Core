# Loop Control Statements

# 1. Pass Statement
for i in range(5):
    pass

count = 5

while count > 0 :
    if count == 3 :
        pass
    else:
        print(count)
    count -= 1

print("_______________________________\n")

# 2. Break Statement
for i in range(5):
    if i == 3:
        break
    print(i) # prints 0 1 2 

print("_______________________________\n")

# 3. Continue Statement
for i in range(10):
    if i == 3:
        continue  # skips where i == 3 (skips one iteration where condition matched)
    print(i)      # prints the remaining Elements i.e:  0 1 2 4 5 6 7 8 9

print("_______________________________\n")

# validate user input using loop
while True:
    user_input = input("Enter 'exit' to stop ")
    if user_input == 'exit':
        print("Great ! You guessed it right.")
        break
    print("Wrong, input : ", user_input)








