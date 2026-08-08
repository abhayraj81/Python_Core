# 1. Limit the decimal places to 2 digits using .format method and print result, for the variable pi = 3.14159265359
pi = 3.14159265359
print("Value of pi upto 2 decimal places {:.2f}".format(pi))
print(f"Value of pi upto 2 decimal places {pi:.2f}")

# 2. Extract characters from index 2 to 8 with a step of 2: Given my_string = "Python Course", slice characters from index 2 to 8, skipping every other char.
my_string = "Python Course"
print(my_string[2:8:2])

# 3.  Slice to get only the middle character(s): For my_string = "Madhav", use slicing to extract the middle character(s).
def mid_str(word):
    middle = int(len(word)/2)
    if len(word)%2 == 0 :
        return word[middle-1:middle+1]
    else:
        return word[middle]

my_string = "Mahadevan" # 9 character 
    #index = 012345678
my_string2 = "Madhav"   # 6 character
    #index =  012345

print(mid_str(my_string))
print(mid_str(my_string2))

#4. Remove the first 3 and last 3 characters: Given my_string = "Regression Analysis", remove the first 3 and last 3 characters.
my_string = "Regression Analysis"
print(my_string[3:-3])

# 5. Get the substring that starts 4 characters from the end to the last character: For my_string = "Classification", slice the string starting from the 4th character from the end to the last character.
my_string = "Classification"
print(my_string[-4:])

# 6. How to Reverse a String Using Python String Methods? 
name = "Abhay Raj"
print(name[::-1])  

#7. Write a Python function to check if a string is a palindrome using string methods.
name  = "mohom"
name2 = "mohom"
name3 = "mohon"
def palindrome(n):
    if n == n[::-1]:
        print(f"{n} is palindrome")
    else:
        print(f"{n} is not palindrome")

palindrome(name2)
palindrome(name3)

