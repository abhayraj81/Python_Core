# 1. Print while loop output in same line
i = 1
while i in range(1,4):
    print(f"Hi ! Abhay {i}", end = " ")
    i += 1 
print()

# 2. star pattern using loop

# 2.1 simple traingle
print("\n2.1 simple traingle\n")
# nested loop method
n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end = " ")
    print()

print("\n---\n")

# shortcut method
n = 5
for i in range(1, n+1):
    print("* " * i)
    

# 2.2 inverted traingle
# nested loop method
print("\n2.2 inverted traingle\n") 
n = 5
for i in range(n,0,-1):
    for j in range(1, i+1):
        print("*", end = " ")
    print()

print("\n---\n")

# shortcut method
for i in range(n,0,-1):
    print("* " * i)


# 2.3 pyramid pattern 
print("\n2.3 pyramid traingle\n") 

n = 5
for i in range(1,n+1):
    print(' ' * (n-i), end = "")
    print("*" * (2*i-1))
    
# 3. WAP to print factorial no a number
def fact(num):
    result = 1
    while num > 0:
        result = result * num
        num = num-1
    return result
print(fact(5))

# 4. WAP to count vowel in a string
def vowelChk(a):
    count = 0
    for char in a:
        if ((char.lower() in vowels) or (char.upper() in vowels)):
            count += 1
    return count
str = input("Enter String to check number of Vowel : ")
vowels = "aeiou"
print("The numbers of vowels are : ",vowelChk(str))

# 5. longest word in a sentence
def longWord(word):
    words = sentence.split()
    longest_Word = ""
    for word in words:
        if len(word) > len(longest_Word):
            longest_Word = word
    return longest_Word
sentence = input("Enter Sentence to check longest word : ")
print("Longest word : ", longWord(sentence))

#6. do while loop in python (we achieve behaviour by while loop)
while True:
    num = int(input("Enter number greater than 10 : "))
    if num > 10 :
        print(f"Valid Number entered : {num}")
        break # when condition satisfied
    else:
        print("Number is not greater than  10 enter again !")

#7. fibonacci sequence
def fibo(n):
    a,b = 0,1
    count = 0 
    while count < n:
        print(a)
        a,b = b, a+b
        count += 1
    return count
num = int(input("Enter number to find fibonacci sequence : "))
print(fibo(num))